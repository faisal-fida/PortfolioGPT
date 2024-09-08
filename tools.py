from langchain_core.tools import Tool

import datetime
import yfinance as yf


def get_current_time(*args, **kwargs):
    """Returns the current time in H:MM AM/PM format."""
    now = datetime.datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')}."

def get_stock_price(symbol: str, current_time: str) -> str:
    """Returns the current price of a stock."""
    try:
        stock = yf.Ticker(symbol)
        price = stock.history(period="1d")["Close"][0]
        return f"The current price of {symbol} is ${price:.2f}. The current time is {current_time}."
    except Exception as e:
        return f"I couldn't find the stock price for that. Error: {e.args[0]}"


# Define the tools that the AI can use
ai_tools = [
    Tool(
        name="Time",
        func=get_current_time,
        description="Useful for when you need to know the current time.",
    ),
    Tool(
        name="Stock Price",
        func=get_stock_price,
        description="Useful for when you need to know the current price of a stock.",
    ),
]