# -*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import Error


class DatabaseManager:
    def __init__(self, host, user, password, database):
        """ 初始化数据库连接 """
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor(dictionary=True)
        print("数据库连接成功！")

    def insert_original_text(self, title, original_text, chapter_number):
        """ 插入记录，只包括标题和原文 """
        query = "INSERT INTO t_storage (title, original_text, chapter_number) VALUES (%s, %s, %s)"
        values = (title, original_text, chapter_number)
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print(f"记录插入成功: {title}")
        except Error as e:
            print(f"插入错误: {e}")

    def insert_username(self, username, newName):
        """ 插入记录，只包括标题和原文 """
        query = "INSERT INTO t_replace (original_text,new_text, type) VALUES (%s, %s, %s)"
        values = (username, newName, 0)
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print(f"记录插入成功: {username}")
        except Error as e:
            print(f"插入错误: {e}")

    def insert_address(self, original_text, new_text):
        """ 插入记录，只包括标题和原文 """
        query = "INSERT INTO t_replace (original_text,new_text, type) VALUES (%s, %s, %s)"
        values = (original_text, new_text, 1)
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print(f"记录插入成功: {original_text}")
        except Error as e:
            print(f"插入错误: {e}")

    def insert_storage(self, title, original_text, modify_text, translation_text, released):
        """ 插入记录 """
        query = "INSERT INTO t_storage (title, original_text, modify_text, translation_text, released) VALUES (%s, %s, %s, %s, %d)"
        values = (title, original_text, modify_text, translation_text, released)
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print("记录插入成功")
        except Error as e:
            print("插入错误：", e)

    def fetch_records(self):
        """ 查询所有记录 """
        try:
            self.cursor.execute("SELECT * FROM t_storage")
            records = self.cursor.fetchall()
            return records
        except Error as e:
            print("查询错误：", e)

    def update_storage(self, id, modify_text):
        """ 更新记录 """
        query = "UPDATE t_storage SET modify_text = %s,  replaced=1 WHERE id = %s"
        values = (modify_text, id)
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print("记录更新成功")
        except Error as e:
            print("更新错误：", e)

    def update_extracted(self, id, extracted):
        """ 更新记录 """
        query = "UPDATE t_storage SET extracted=%s WHERE id = %s"
        values = (extracted, id)
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print("记录更新成功")
        except Error as e:
            print("更新错误：", e)
    def update_translated(self, id, translation_text,translated):
        """ 更新记录 """
        query = "UPDATE t_storage SET translation_text=%s, translated=%s WHERE id = %s"
        values = (translation_text, translated, id)
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print("记录更新成功")
        except Error as e:
            print("更新错误：", e)
    def update_translated_title(self, id, translation_title):
        """ 更新记录 """
        query = "UPDATE t_storage SET translation_title=%s WHERE id = %s"
        values = (translation_title, id)
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print("记录更新成功")
        except Error as e:
            print("更新错误：", e)
    def delete_record(self, id):
        """ 删除记录 """
        query = "DELETE FROM t_storage WHERE id = %s"
        try:
            self.cursor.execute(query, (id,))
            self.connection.commit()
            print("记录删除成功")
        except Error as e:
            print("删除错误：", e)

    def fetch_unreleased_records(self):
        """获取所有released=0的记录，并按chapter_number升序排列"""
        query = "SELECT id, title, original_text,modify_text,translation_text, released,replaced, chapter_number FROM t_storage WHERE released = 0 ORDER BY chapter_number ASC"
        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()  # 获取所有匹配的记录
            return records
        except Error as e:
            print(f"查询错误: {e}")

    def fetch_unreplace_records(self):
        """获取所有released=0的记录，并按chapter_number升序排列"""
        query = "SELECT id, title, original_text,modify_text,translation_text, released,replaced, chapter_number FROM t_storage WHERE replaced = 0 ORDER BY chapter_number ASC"
        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()  # 获取所有匹配的记录
            return records
        except Error as e:
            print(f"查询错误: {e}")

    def fetch_un_extracted_records(self):
        """获取所有released=0的记录，并按chapter_number升序排列"""
        query = "SELECT id, title, original_text,modify_text,translation_text, released,replaced, chapter_number FROM t_storage WHERE extracted = 0 ORDER BY chapter_number ASC"
        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()  # 获取所有匹配的记录
            return records
        except Error as e:
            print(f"查询错误: {e}")
    def fetch_un_translation_records(self):
        """获取所有released=0的记录，并按chapter_number升序排列"""
        query = "SELECT id, title, original_text,modify_text,translation_text, released,replaced, chapter_number FROM t_storage WHERE translated = 0 ORDER BY chapter_number ASC"
        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()  # 获取所有匹配的记录
            return records
        except Error as e:
            print(f"查询错误: {e}")

    def fetch_un_translation_title_records(self):
        """获取所有released=0的记录，并按chapter_number升序排列"""
        query = "SELECT id, title, original_text,modify_text,translation_text,translation_title, released,replaced, chapter_number FROM t_storage WHERE translation_title IS NULL ORDER BY chapter_number ASC"
        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()  # 获取所有匹配的记录
            return records
        except Error as e:
            print(f"查询错误: {e}")

    def fetch_username(self, username):
        """获取所有released=0的记录，并按chapter_number升序排列"""
        query = "SELECT id, type, original_text, new_text FROM t_replace WHERE original_text = %s and type = 0 "
        try:
            self.cursor.execute(query, (username,))
            record = self.cursor.fetchone()  # 获取匹配的记录
            return record
        except Error as e:
            print(f"查询错误: {e}")

    def fetch_address(self, address):
        """获取所有released=0的记录，并按chapter_number升序排列"""
        query = "SELECT id, type, original_text, new_text FROM t_replace WHERE original_text = %s and type = 1 "
        try:
            self.cursor.execute(query, (address,))
            records = self.cursor.fetchall()  # 获取所有匹配的记录
            return records
        except Error as e:
            print(f"查询错误: {e}")

    def fetch_all_usernames(self):
        """获取所有released=0的记录，并按chapter_number升序排列"""
        query = "SELECT id, type, original_text, new_text FROM t_replace WHERE type = 0 and del_flag=0"
        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()  # 获取所有匹配的记录
            return records
        except Error as e:
            print(f"查询错误: {e}")

    def close(self):
        """ 关闭数据库连接 """
        self.cursor.close()
        self.connection.close()
        print("数据库连接已关闭")
