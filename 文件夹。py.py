# _*_ coding:utf-8 _*_
import os
#获取当前路径
print(os.getcwd())
# os.getcwd()
#列出当前或者指定目录下的文件或者文件夹
# print(os.listdir("D:/"))
#判断是否是一个文件，是否存在

# print(os.path.isfile(".//file.py"))
# print(os.path.exists("..//第六课循"))
#文件重新命名
# os.rename("python","123.txt")
print(os.path.split("D:\pycharm\第十课文件操作\123.txt"))

#创建文件夹
# os.mkdir("xx")
#
print(os.path.getsize("file.py"))
