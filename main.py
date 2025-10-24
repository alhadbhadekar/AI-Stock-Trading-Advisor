import os
os.environ["CREW_SHOW_TRACE"] = "false"

from dotenv import load_dotenv
from crew import stock_crew
from tools.stock_research_tool import get_stock_price_func
import re

load_dotenv()


def _extract_stock_analysis(text: str) -> str:
    """Extract structured stock summary (Stock → Momentum) if present in Crew output."""
    if not text:
        return ""
    match = re.search(
        r"(Stock\s*:\s*.*?(Momentum\s*:\s*[^\n]+))",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if match:
        return match.group(1).strip()
    return text.strip()


def _normalize_results(result):
    """Normalize CrewAI output into {analysis, decision}."""
    if isinstance(result, dict):
        return {
            "analysis": _extract_stock_analysis(str(result.get("analysis", "")).strip()),
            "decision": str(result.get("decision", "")).strip(),
        }

    raw_output = str(result).strip()
    separator = "--- TRADING DECISION ---"
    if separator in raw_output:
        parts = raw_output.split(separator, 1)
        return {
            "analysis": _extract_stock_analysis(parts[0].strip()),
            "decision": (separator + parts[1]).strip(),
        }

    return {"analysis": _extract_stock_analysis(raw_output), "decision": ""}


def run(stock_symbol: str):
    """
    Run Analyst first. If ticker is invalid, DO NOT run Trader.
    If data is valid, run Trader.
    """
    try:
        # Step 1: Always fetch analyst summary first
        analyst_summary = get_stock_price_func(stock_symbol)

        # ✅ If analyst summary indicates symbol invalid → RETURN ONLY ANALYSIS
        if analyst_summary.startswith("Could not retrieve data for"):
            return {
                "analysis": analyst_summary.strip(),
                "decision": (
                    f"⚠️ No trading recommendation was generated because '{stock_symbol}' is not a valid stock symbol.\n\n"
                    f"🔎 You can search for the correct ticker here:\n"
                    f"https://finance.yahoo.com/lookup"
                )
            }

        # ✅ If valid stock → run Trader
        crew_result = stock_crew.kickoff(inputs={
            "stock": stock_symbol,
            "context": analyst_summary
        })
        normalized = _normalize_results(crew_result)

        normalized["analysis"] = analyst_summary.strip()
        return normalized

    except Exception as e:
        error_text = str(e)

        # ✅ Detect Groq rate-limit errors explicitly
        if "RateLimitError" in error_text or "rate_limit_exceeded" in error_text:
            return {
                "analysis": analyst_summary.strip(),
                "decision": (
                    "⚠️ Groq rate limit exceeded — wait 1–3 minutes and try again."
                ),
            }

        # Generic fallback
        return {
            "analysis": f"Error during crew run: {error_text}",
            "decision": "",
        }

