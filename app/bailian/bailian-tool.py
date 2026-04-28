# from langchain_core.tools import Tool
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from app.bailian.common import chat_prompt_template, llm

class AddInputArgs(BaseModel):
    a: int = Field(description="The first number to add.")
    b: int = Field(description="The second number to add.")
@tool(
    description="add two numbers",
    # 定义工具类的类型
    args_schema=AddInputArgs
)
# 1 开发工具函数
def add(a, b):
    """Add two numbers."""
    return a + b

# 2. 将工具函数转化为langchain tool 对象
# add_tools = Tool.from_function(
#     name="add",
#     description="add two numbers",
#     func=add,
#     args_schema=None
# )

# 3. 定义工具字典（代码调用用）
tool_dict = {
    "add": add
}


llm_with_tools = llm.bind_tools([add])

chain = chat_prompt_template | llm_with_tools

resp = chain.invoke(input={"role": "计算", "domain": "数学计算", "question": "使用工具计算：100+100=?"})
print(resp)

for tool_calls in resp.tool_calls:
    print(tool_calls)

    args = tool_calls['args']
    print(args)

    func_name = tool_calls['name']
    print(func_name)

    tool_func = tool_dict[func_name]
    tool_content = tool_func.invoke(args)
    print(tool_content)
