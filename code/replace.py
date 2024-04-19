# -*- coding: utf-8 -*-
from database_manager import DatabaseManager
import time
from langchain_openai import ChatOpenAI

import os
from langchain_openai import ChatOpenAI
from my_handler import MyHandler
from tenacity import retry, stop_after_attempt, wait_fixed
os.environ['OPENAI_API_KEY'] = 'sk-ZRGxqeGOAugc32bKA1529c37D92443E2A27a54De3eE87fCc'
# os.environ['OPENAI_API_BASE'] = "https://api.freegpt.art/v1"
# os.environ['OPENAI_BASE_URL'] = "https://api.freegpt.art/v1"
os.environ['OPENAI_API_BASE'] = "http://localhost:3040/v1"
os.environ['OPENAI_BASE_URL'] = "http://localhost:3040/v1"


@retry(stop=stop_after_attempt(50), wait=wait_fixed(2))
def replaceUsernameAndAddress():
    # 初始化数据库连接
    db_manager = DatabaseManager('localhost', 'root', '123456', 'test')
    handler = MyHandler()
    #llm = ChatOpenAI(model='text-davinci-003', temperature=0)
    llm = ChatOpenAI(temperature=0)
    records = db_manager.fetch_un_extracted_records()
    for record in records:
        handler.handler_name(db_manager, llm, record)
        db_manager.update_extracted(record['id'], 1)
        # newText = handler.rewrite(replace)
        # translate_text = handler.translate(replace)
        # db_manager.update_record(record['id'], replace, translate_text)
    # 关闭数据库连接
    db_manager.close()


replaceUsernameAndAddress()
