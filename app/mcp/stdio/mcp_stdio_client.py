
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent 
from app.bailian.common import llm
import asyncio
async def create_mac_stdio_client():
    server_params = StdioServerParameters(
        command="python",
        args=["/Users/xinghaodong/Desktop/AI/AIAgent/ai-agent-test/app/mcp/stdio/mcp_stdio_client.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)  # 自动加载MCP服务器提供的工具
            agent = create_agent(llm, tools)  # 创建React Agent
            # agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
            response = await agent.ainvoke(input={"messages": [("user", "what's (3 + 5) x 12?")]})  # 调用Agent
            print(response)


asyncio.run(create_mac_stdio_client())

# agent = create_react_agent(llm, tools)  # 创建React Agent
# response = await agent.ainvoke(input={"messages": [("user", "what's (3 + 5) x 12?")]})  # 调用Agent
