from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatMessagePromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from pydantic import BaseModel, Field
llm = ChatOpenAI(
    model="qwen3.6-plus",
    # api_key="sk-ffabef30d4b145deb70463a0105d6f3c",
    api_key=SecretStr("sk-ffabef30d4b145deb70463a0105d6f3c"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    streaming=True,
)
# ChatMessagePromptTemplate
system_template = ChatMessagePromptTemplate.from_template(
    template="你是一位{role}专家,擅长回答{domain}领域的问题。",
    role="system",
)
human_template = ChatMessagePromptTemplate.from_template(
    template="用户问题:{question}",
    role="human",
)
chat_prompt = ChatPromptTemplate.from_messages([
    system_template,
    human_template,
])


chat_prompt_template = ChatPromptTemplate.from_messages([
("system", "你是一位{role}专家，擅长回答{domain}领域的问题"),
("user", "用户问题{question}")
])

class AddInputArgs(BaseModel):
a: int = Field(description="first number")
b: int = Field(description="second number")
@tool(
    description="add two numbers",
    args_schema=AddInputArgs,
    return_direct=True,
)
def add(a, b):
    """add two numbers"""
    return a + b
def create_calc_tools():
    return [add]
    
calc_tools = create_calc_tools()