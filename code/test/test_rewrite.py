import os

os.environ['OPENAI_API_KEY'] = 'test'
os.environ['OPENAI_API_BASE'] = "http://localhost:3040/v1"
os.environ['OPENAI_BASE_URL'] = "http://localhost:3040/v1"
from langchain_openai import ChatOpenAI
from database_manager import DatabaseManager

# 导入LangChain中的提示模板
from langchain_core.prompts import PromptTemplate

text = """
江城机场。
人来人往。
一个着一袭白色长裙的女孩走出通道。
女孩一头墨发及腰，拉着行李箱站在人群中看着这久违的机场，脸上挂着浅浅的笑。
她本就长得漂亮，这一笑更是惹人侧目。
清纯，甜美，是很多男生心目中的初恋白月光形象，尽管她现在已经有二十三岁。
走出机场，坐上出租车。


"""
# 创建原始模板
template = """
请重写这段内容：{text}
"""

from langchain.output_parsers import CommaSeparatedListOutputParser

# 创建模型实例
llm = ChatOpenAI(model="text-davinci-002", max_tokens=5000)

# 设置模板
output_parser = CommaSeparatedListOutputParser()
prompt = PromptTemplate.from_template(template)

# 回答
chain = prompt | llm
answer = chain.invoke({'text': text})
print("answer=", answer)


# 设置为本地的模型，因为vicuna使用的是假名字"text-embedding-ada-002"
# chat = ChatOpenAI(model="text-embedding-ada-002",temperature=0)
# answer = chat.invoke("Translate this sentence from English to Chinese. I love programming.")
# print(answer)
