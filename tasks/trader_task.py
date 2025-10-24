# trader_task.py (Make sure this matches the screenshot's output)
from crewai import Task
from agents.trader_agent import trader_agent

trade_decision = Task(
    description=(
        "Based ONLY on the Analyst's analysis (provided as context), make a clear trading decision for {stock}: "
        "Buy, Sell, or Hold. Consider price direction, daily % change, day high/low, and volume.\n\n"
        "IMPORTANT: Your output MUST begin with the unique separator: '--- TRADING DECISION ---\n\n' "
        "Followed by the Output format:\n"
        "Recommendation: <BUY|SELL|HOLD>\n"
        "Reason: <one concise paragraph, 2-4 sentences>\n"
        "Do not repeat the analyst details verbatim. No extra sections."
    ),
    expected_output=(
        "--- TRADING DECISION ---\n\n"
        "Recommendation: BUY|SELL|HOLD\n"
        "Reason: <one short paragraph>"
    ),
    agent=trader_agent,
    context_keys=["analysis"],
    output_key="decision",    
    return_output=True
)