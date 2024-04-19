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
    records = db_manager.fetch_un_translation_records()
    for record in records:
        translation_text = handler.translate(record['modify_text'])
        print(translation_text)
        db_manager.update_translated(record['id'], translation_text, 1)
        # time.sleep(10)
    # 关闭数据库连接
    db_manager.close()

translate()
