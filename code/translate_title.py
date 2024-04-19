# -*- coding: utf-8 -*-
from database_manager import DatabaseManager
from my_handler import MyHandler
from tenacity import retry, stop_after_attempt, wait_fixed

import time
@retry(stop=stop_after_attempt(50), wait=wait_fixed(10))
def translate():
    # 初始化数据库连接
    db_manager = DatabaseManager('localhost', 'root', '123456', 'test')
    handler = MyHandler()
    records = db_manager.fetch_un_translation_title_records()
    for record in records:
        translation_title = handler.translate(record['title'])
        print(translation_title)
        db_manager.update_translated_title(record['id'], translation_title)
        # time.sleep(10)
    # 关闭数据库连接
    db_manager.close()

translate()
