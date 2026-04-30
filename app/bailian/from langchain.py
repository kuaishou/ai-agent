from langchain.agents import create_structured_chat_agent
from langchain.agents import AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from app.bailian.common import create_calc_tools, llm

# Create the agent using the new LangChain v0.1+ API
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个有用的助手，拥有以下可用工具:\n{tool_names}\n\n按照以下格式回答:\n```json\n{{\"name\": \"工具名称\", \"args\": {{...}}}}\n```\n\n如果不需要使用工具，直接回答问题。"),
    ("human", "{input}"),
    ("agent_info", "{agent_info}")
])

# Create agent
agent = create_structured_chat_agent(
    llm=llm,
    tools=create_calc_tools(),
    prompt=prompt,
)

# Create agent executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=create_calc_tools(),
    verbose=True,
)

resp = agent_executor.invoke({"input": "100+100=?"})
print(resp)
print(resp["output"])