import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))  # 把项目根目录加入路径

from langchain_core.tools import tool
from langchain_core.output_parsers import StrOutputParser  # 新增导入
from pydantic import BaseModel, Field
from app.bailian.common import chat_prompt_template, llm


parser = StrOutputParser()
chain = chat_prompt_template | llm | parser

resp = chain.invoke(input={"role": "计算", "domain": "数学计算", "question": "使用工具计算：100+100=?"})
print(resp)