import yfinance as yf
from crewai.tools import tool

@tool("Live Stock Information Tool")
def get_stock_price(stock_symbol: str) -> str:
    """
    Retrieves the latest stock price and other relevant info for a given stock symbol using Yahoo Finance.

    Parameters:
        stock_symbol (str): The ticker symbol of the stock (e.g., AAPL, TSLA, MSFT).

    Returns:
        str: A summary of the stock's current price, daily change, and other key data.
    """

    stock = yf.Ticker(stock_symbol)
    info = stock.info

    current_price = info.get("regularMarketPrice")
    change = info.get("regularMarketChange")
    change_percent = info.get("regularMarketChangePercent")
    currency = info.get("currency")

    if current_price is None:
        return f"Could not retrieve data for stock symbol '{stock_symbol}'. Please check the symbol and try again."
    
    return (
        f"Stock: {stock_symbol.upper()}\n"
        f"Price: {current_price} {currency}\n"
        f"Day High: {info.get('dayHigh')}\n"
        f"Day Low: {info.get('dayLow')}\n"
        f"Change: {change} ({round(change_percent, 2)}%)"
    )


def get_stock_price_func(stock_symbol: str) -> str:
    """
    Retrieves the latest stock price and other relevant info for a given stock symbol using Yahoo Finance.

    Parameters:
        stock_symbol (str): The ticker symbol of the stock (e.g., AAPL, TSLA, MSFT).

    Returns:
        str: A summary of the stock's current price, daily change, and other key data.
    """

    stock = yf.Ticker(stock_symbol)
    info = stock.info

    current_price = info.get("regularMarketPrice")
    change = info.get("regularMarketChange")
    change_percent = info.get("regularMarketChangePercent")
    currency = info.get("currency")

    if current_price is None:
        return f"Could not retrieve data for stock symbol '{stock_symbol}'. Please check the symbol and try again."
    
    return (
        f"Stock: {stock_symbol.upper()}\n"
        f"Price: {current_price} {currency}\n"
        f"Day High: {info.get('dayHigh')}\n"
        f"Day Low: {info.get('dayLow')}\n"
        f"Change: {change} ({round(change_percent, 2)}%)"
    )

# print(get_stock_price("AAPL"))