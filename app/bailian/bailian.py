import os
from openai import OpenAI

client = OpenAI(
    # 直接写你的API Key，不要用 os.getenv()
    api_key="sk-ffabef30d4b145deb70463a0105d6f3c",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    model="qwen3.6-plus",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁？"},
    ]
)
print(completion.model_dump_json())