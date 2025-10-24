from crewai import Task
from agents.analyst_agent import analyst_agent

get_stock_analysis = Task(
    description=(
        "Analyze the performance of the stock {stock}. "
        "Use the live stock information tool to retrieve current price, daily change %, day high/low, and volume. "
        "Provide a structured summary in plain English.\n\n"
        "OUTPUT RULES:\n"
        "1. No Thought, Action, or Observation sections.\n"
        "2. No markdown, no bullet points.\n"
        "3. Use short factual sentences in this format:\n\n"
        "Stock: AAPL\n"
        "Current price: 182.01 USD\n"
        "Daily change: +0.44%\n"
        "Day high / low: 183.20 / 181.50\n"
        "Volume: 51,853,339\n"
        "Momentum: Slight upward bias"
    ),
    expected_output=(
        "A plain English summary of five factual lines covering: "
        "stock symbol, current price, daily change, high/low, volume, and short-term momentum."
    ),
    agent=analyst_agent,
    output_key="analysis",
    return_output=True
)