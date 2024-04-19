import deepl
#
# from my_handler import MyHandler
#
# handler = MyHandler()
# print(handler.translate("你好"))


from PyDeepLX import PyDeepLX
# By default, the source language is automatically recognized and translated into English without providing any alternative results.
print(PyDeepLX.translate("你好世界")) # Return String
