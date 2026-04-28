from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatMessagePromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage, HumanMessage,AIMessage,ToolMessage

llm = ChatOpenAI(
    model="qwen3.6-plus",
    # api_key="sk-ffabef30d4b145deb70463a0105d6f3c",
    api_key=SecretStr("sk-ffabef30d4b145deb70463a0105d6f3c"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    streaming=True,
)
# resp = llm.stream("你是谁？")
# for chunk in resp:
#     print(chunk.content, end="", flush=True)

# 1、创建一个提升词模版
# prompt_template = PromptTemplate.from_template("今天{something}真不错")
# # 2、模版+变量=》提示词
# promt=prompt_template.format(something="天气")
# print(promt)




# chat_prompt_template = ChatPromptTemplate.from_messages([
# ("system", "你是一位{role}专家，擅长回答{domain}领域的问题"),
# ("user", "用户问题{question}")
# ])
# # 2、模版+变量=》提示词
# promt=chat_prompt_template.format_messages(role="编程", domain="web开发", question="如何构建一个基于vue的前端应用")
# resp = llm.stream(promt)
# for chunk in resp:
#     print(chunk.content, end="", flush=True)


# ChatMessagePromptTemplate
# system_template = ChatMessagePromptTemplate.from_template(
#     template="你是一位{role}专家,擅长回答{domain}领域的问题。",
#     role="system",
# )
# human_template = ChatMessagePromptTemplate.from_template(
#     template="用户问题:{question}",
#     role="human",
# )
# chat_prompt = ChatPromptTemplate.from_messages([
#     system_template,
#     human_template,
# ])
# messages = chat_prompt.format_messages(
#     role="技术",
#     domain="web开发", 
#     question="如何构建一个基于vue的前端应用"
# )
# print(messages)

# FewShotPromptTemplate通过提示词实现大模型少样本学习 
example_template = "输入：{input}\n输出：{output}"
examples=[
    {"input": "将‘Hello World’翻译成中文","output": "你好，世界！"},
    {"input": "将‘goodbye’翻译成中文","output": "再见"},
]
few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=PromptTemplate.from_template(example_template),
    prefix="请将以下英文翻译成中文",
    suffix="输入：{text}\n输出：",
    input_variables=["text"],
    example_separator="\n",
)
prompt = few_shot_prompt_template.format(text="Thank you for your help.")
# print(few_shot_prompt_template.format(text="hello world"))
resp = llm.stream(prompt)
for chunk in resp:
    print(chunk.content, end="", flush=True)