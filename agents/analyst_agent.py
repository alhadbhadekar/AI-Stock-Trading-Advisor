from crewai import Agent, LLM
from tools.stock_research_tool import get_stock_price

# Initialize LLM
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.0
)

analyst_agent = Agent(
    role="Financial Market Analyst",
    goal=(
        "Deliver a clear, factual, and concise market summary for a given stock "
        "based on live data retrieved from the stock tool."
    ),
    backstory=(
        "You are a senior financial analyst with deep expertise in market performance evaluation. "
        "You specialize in interpreting real-time stock metrics—price, daily change %, high/low, and volume—"
        "and summarizing them into professional-grade insights."
    ),
    llm=llm,
    tools=[get_stock_price],
    verbose=False,
    allow_delegation=False,
    max_iter=1  # ensure single-pass, no Thought/Action logs
)