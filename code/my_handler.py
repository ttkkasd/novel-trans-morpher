# -*- coding: utf-8 -*-
import os
from langchain.output_parsers import CommaSeparatedListOutputParser

from langchain_openai import ChatOpenAI
from database_manager import DatabaseManager
import time
# 导入LangChain中的提示模板
from langchain_core.prompts import PromptTemplate
import deepl
import requests
from urllib.parse import quote
from PyDeepLX import PyDeepLX

class MyHandler:
    def __init__(self):
        print('init')

    def check_string_lengths(self, strings):
        """
        检查字符串数组中每个字符串的长度是否小于等于3。

        参数:
        strings (list of str): 需要检查的字符串列表。

        返回:
        list of bool: 对应每个字符串长度是否小于等于3的布尔值列表。
        """
        return [len(s) <= 3 for s in strings]

    def handle_large_text(self, llm, output_parser, text):
        # 检查文本长度是否超过3000字符
        if len(text) > 3000:
            # 分割文本为小于3000字符的部分
            parts = [text[i:i + 3000] for i in range(0, len(text), 3000)]
        else:
            # 如果文本不超过3000字符，直接放入数组处理
            parts = [text]

            # 解析结果集合
        all_names = set()

        # 对每个部分使用llm处理并提取人名
        for part in parts:
            # 假设 handler_username 是以文本作为输入，返回用户名列表的方法
            names = self.handler_username(llm, part, output_parser)
            # 将新提取的名字添加到结果集合中，使用集合自动去重
            all_names.update(names)
        # 将集合转换回列表
        return list(all_names)

    def handler_username(self, llm, text, output_parser):

        # 处理人名 >>>>>>>>
        # 创建原始模板
        # 请帮我写一个满足下列需求的Prompt:
        # 需求
        # ===
        # 在下列文本中提取出所有具体的人物名称。 文本内容：{text}。
        # 要求
        # ===
        # 1.只需提取具体的人名，无论是中国人的名字还是外国人的名字。
        # 2.不要提取含有称谓的名字，例如这些称谓是不符合要求的：夫人、族长、阿姨、大哥、女神、父、母等。
        # 3.人名至少2个字以上，只含有一个姓氏的不要，例如“许”。
        # 4.只需列出人名，用逗号隔开，并省略任何无关的回答。不需要包括拼音。
        template = """
        Please extract all standard personal names from the provided text: {text}. Requirements: 1. Extract only specific personal names, whether they are Chinese or foreign. 2. Do not extract names that include any form of title or nickname, especially names containing but not limited to titles such as 'Mrs.', 'tribal chief', 'aunt', 'big brother', 'goddess', 'father', 'mother', including similar titles like '慕父', '慕母'. Nicknames like '兮兮', '华华' are also unacceptable. Carefully distinguish between proper names, nicknames, and titles, as only specific personal names are required. 3. Names must be at least two characters long and should not consist solely of a surname, such as '许'. 4. List only the names, separated by commas, and omit any irrelevant responses. There is no need to include pinyin. 5. Reflect and verify the components of standard personal names, ensuring not to include any that contain nicknames or titles.
        """
        # 设置模板
        prompt = PromptTemplate.from_template(template)
        # 回答
        chain = prompt | llm
        answer = chain.invoke({'text': text})
        print("answer=", answer)
        # 解析名字
        names = output_parser.parse(answer.content)
        print("names=", names)
        return names

    def handler_name(self, db, llm, record):
        text = record['original_text']
        output_parser = CommaSeparatedListOutputParser()

        names = self.handle_large_text(llm, output_parser, text)
        # while self.check_string_lengths(names):
        #     names = self.handler_username(llm, text, output_parser)
        # 重命名
        renameTemplate = """
        Please rename the name '{name}' while adhering to the following conditions: 1. Retain the original surname and ensure the new given name has the same number of characters as the original. For example, if the original name is '路言兮', the new name might be '路非语'; if the original name is '宋淮', the new name could be '宋泽'. 2. Important: Respond only with the new name, without any additional comments or answers.
        """
        renamePrompt = PromptTemplate.from_template(renameTemplate)
        renameChain = renamePrompt | llm

        for username in names:
            # time.sleep(0.5)
            record = db.fetch_username(username)
            if record is not None:
                # 替换文章中原来的名字
                text = text.replace(username, record['new_text'])
            else:
                newText = renameChain.invoke({'name': username})
                db.insert_username(username, newText.content)

        # # >>>> 处理城市名称
        # extractAddressTemplate = """
        # Please extract all the city names from the text below. The response should only include the specific names, without any additional content. List the names separated by commas.:{text}
        # """
        # # 设置模板
        # extractAddressPrompt = PromptTemplate.from_template(extractAddressTemplate)
        # # 回答
        # addressChain = extractAddressPrompt | llm
        # extractAddressAnswer = addressChain.invoke({'text': text})
        # print("extractAddressAnswer=", extractAddressAnswer)
        # # 解析名字
        # addressList = output_parser.parse(extractAddressAnswer.content)
        # print("addressList=", addressList)
        # # 重命名
        # renameAddressTemplate = """
        # Rename the given city name ('{name}') following these guidelines: 1. Respond only with the new city name, excluding any other unrelated content. 2. The new name must adhere to typical city naming conventions. 3. If the original name contains the character '城', the new name must also include '城'. 4. If the city name is in Chinese, the new name must also be in Chinese, and the number of characters in the new name should match the original. Please review your response to ensure it meets all these requirements. Respond with only the new city name.
        # """
        # renameAddressPrompt = PromptTemplate.from_template(renameAddressTemplate)
        # renameAddressChain = renameAddressPrompt | llm
        # for address in addressList:
        #     records = db.fetch_address(address)
        #     newText = renameAddressChain.invoke({'name': address})
        #     if records is not None and len(records) > 0:
        #        db.insert_address(address, newText.content)
        #     # 替换文章中原来的名字
        #     text = text.replace(address, newText.content)

        return text

    def rewrite(self, replace_text):
        llm = ChatOpenAI(model="gpt-3.5-turbo-16k-0613")
        # 请帮我写一个满足下列要求的prompt: 重写故事。要求：只需要重新用更合适内容的方式去复述故事的主要内容，不要变更内容中出现的人名和地名。不要删减故事内容。
        transfer_template = """
        Please rewrite the story, ensuring that the main content is retold in a more suitable manner. Do not change the names of any people or places mentioned in the content. Additionally, ensure that no part of the story’s content is omitted. The objective is to improve the narrative style while preserving all original details. \n content :{content}
        """
        transfer_prompt = PromptTemplate.from_template(transfer_template)
        chain = transfer_prompt | llm
        print("transfer_prompt", transfer_prompt)
        newText = chain.invoke({'content': replace_text})
        # newText = chain.invoke("你好吗")
        print("rewrite==", newText.content)
        return newText.content

    # def translate(self, text):
    #     result = translator.translate_text(text, target_lang="EN-US")
    #     return result.text

    def translate(self, text):

        return PyDeepLX.translate(text)
        # url = "https://api-free.deeplx.net/v2/translate"
        # payload = {
        #     "text": text,
        #     "target_lang": "EN-US"
        # }
        #
        # response = requests.request("POST", url, json=payload)
        # trans = eval(response.text)
        # return trans['translations'][0]['text']
