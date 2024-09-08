from dotenv import load_dotenv
from langchain import hub
import os

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANGCHAIN_ENDPOINT"] = os.getenv("LANGCHAIN_ENDPOINT")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Portfolio API URL to fetch the portfolio data for the llm model
portfolio_api = os.getenv("PORTFOLIO_API")

llm_model = os.getenv("LLM_MODEL")
initial_message = os.getenv("INITIAL_PROMPT")
prompt = hub.pull(
    "hwchase17/structured-chat-agent", api_key=os.environ["LANGCHAIN_API_KEY"]
)
