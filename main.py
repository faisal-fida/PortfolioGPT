from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

# groq
from langchain_groq import ChatGroq

from app.config import system_prompt, llm_model
from app.toolkit import PortfolioToolkit
from app.portfolio_agent.api_wrapper import PortfolioAPIWrapper

api_wrapper = PortfolioAPIWrapper()
toolkit = PortfolioToolkit(api_wrapper=api_wrapper)
tools = toolkit.get_tools()


query = "What are the skills, types of works, and resume URL of Faisal?"


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

llm = ChatGroq(model=llm_model, temperature=0.5)
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

agent_executor.invoke({"input": query})
