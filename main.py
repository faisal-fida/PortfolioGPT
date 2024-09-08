# from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
# from langchain_groq import ChatGroq
# from langchain.memory import ConversationBufferMemory
# from langchain.agents import AgentExecutor, create_structured_chat_agent

from app.config import initial_message, prompt, llm_model

from app.toolkit import PortfolioToolkit
from app.portfolio_agent.api_wrapper import PortfolioAPIWrapper

print("Portfolio")

api_wrapper = PortfolioAPIWrapper()
toolkit = PortfolioToolkit(api_wrapper=api_wrapper)


print("Portfolio Toolkit:", toolkit.get_tools())


# def create_agent():
#     llm = ChatGroq(
#         model=llm_model, temperature=0, max_tokens=None, timeout=None, max_retries=2
#     )
#     memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
#     agent = create_structured_chat_agent(llm=llm, tools=ai_tools, prompt=prompt)
#     agent_executor = AgentExecutor.from_agent_and_tools(
#         agent=agent, tools=ai_tools, verbose=True, handle_parsing_errors=True
#     )
#     memory.chat_memory.add_message(SystemMessage(content=initial_message))
#     return agent_executor, memory


# agent_executor, memory = create_agent()


# while True:
#     user_input = input("User: ")
#     memory.chat_memory.add_message(HumanMessage(content=user_input))

#     response = agent_executor.invoke({"input": user_input})
#     response = response["output"] if response.get("output") else None

#     if response:
#         print(f"AI: {response['output']}")
#         memory.chat_memory.add_message(AIMessage(content=response["output"]))
