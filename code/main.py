# -*- coding: utf-8 -*-
# 文件名: main.py

from database_manager import DatabaseManager

# 创建DatabaseManager实例
db_manager = DatabaseManager('localhost', 'root', '123456', 'test')

# 插入记录
db_manager.insert_record(2, 'Good morning', '早上好', 1)

# 查询所有记录
records = db_manager.fetch_records()
for record in records:
    print(record)

# 关闭数据库连接
db_manager.close()

