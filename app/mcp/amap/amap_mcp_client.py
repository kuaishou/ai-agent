from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import initialize_agent, AgentType
from app.bailian.common import llm,PromptTemplate,file_tools
from langchain_openai import ChatOpenAI  # 示例：假设使用 OpenAI，可根据实际模型调整
import os
import asyncio

# 假设 llm 已配置，这里以 OpenAI 为例，请根据实际需求替换为正确的 LLM 初始化方式
llm = ChatOpenAI(model="gpt-4o", temperature=0)

async def create_mcp_client():
    # amap_key = os.environ.get("AMAP_KEY")
    amap_key = '05a5cdfa24f7a0d25cd7851e28e539b6'

    client = MultiServerMCPClient({
        "amap": {
            "url": f"https://mcp.amap.com/sse?key={amap_key}",
            "transport": "sse",
        }
    })

    tools = await client.get_tools()
    # print(tools)

    return client, tools

async def create_and_run_agent():
    client, tools = await create_mcp_client()
    
    agent = initialize_agent(
        tools=tools+file_tools,
        llm=llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    prompt_template = PromptTemplate.from_template(
        "你是一个智能助手，可以调用高德 MCP 工具。\n\n问题: {input}"
    )

    prompt = prompt_template.format(input="""
    - 我五月底端午节计划去杭州游玩4天。
    - 帮制作旅行攻略，考虑出行时间和路线，以及天气状况路线规划。
    - 制作网页地图自定义绘制旅游路线和位置。
    - 网页使用简约美观页面风格，景区图片以卡片展示。
    - 行程规划结果在高德地图app展示，并集成到h5页面中。
    - 同一天行程景区之间我想打车前往。
    """)
    print(prompt)
    resp=await agent.invoke(prompt)
    print(resp)

    # 此处可继续添加调用 agent 的逻辑
    # result = await agent.arun("你的问题")
    # print(result)
create_and_run_agent()
# if __name__ == "__main__":
#     asyncio.run(create_and_run_agent())