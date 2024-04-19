import os
from database_manager import DatabaseManager
import re


def replace():
    # 初始化数据库连接
    db_manager = DatabaseManager('localhost', 'root', '123456', 'test')
    names = db_manager.fetch_all_usernames()
    storages = db_manager.fetch_unreplace_records()

    # 遍历排序后的文件列表
    for storage in storages:
        original_text = storage['original_text']
        for name in names:
            original_name = name['original_text']
            new_name = name['new_text']
            original_text = original_text.replace(original_name, new_name)
        db_manager.update_storage(storage['id'], original_text)

    # 关闭数据库连接
    db_manager.close()


replace()
