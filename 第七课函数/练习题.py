# -*- coding:utf-8 -*-
'''
排序
'''

# def compare(x,y):
#     if x<y:
#         return x
#     else:
#         return y
# def paiXu():

#判断输入的数字是否大于五个
# def shuRu(list):
#     # 判断输入的数字是否大于五个
#     if len(list)>=5:
#         return True
#     else:
#         return False
# def main():
#     while True:
#         n = input("请输入至少五个数：")
#         list =str(n).split(",")
#         print(list)
#         print("排序如下")
#         if shuRu(list):
#             list01 = [int(j) for j in list]
#             list02 =[]
#             for i in range(len(list01)):
#                 list02.append(min(list01))
#                 list01.remove(min(list01))
#             print(list02)
#             break
#         else:
#             print("输入有误，请重新输入")
# main()

# def cutList(lst):
#         rt = []
#         n = 0
#         for i in range(len(lst)-1):
#                 if lst[i] != lst[i+1]:
#                         rt.append(lst[n:i+1])
#                         n = i+1
#         rt.append(lst[n:])
#         return rt
# def main():
#         lst = [1, 1, 0, 2, 2, 2, 4, 3, 3, 4,2, 0, 0]
#         print(cutList(lst))
# main()


'''
numpy
'''
# import numpy as np
# import random
# #第一小问
# aary = np.random.randint(1,100,size=24)
# aary01= aary.reshape(2,3,4)
# print(aary01)
# print(aary01.shape)
# # #第二小问
# arry02 = np.zeros((8,8))
# print(arry02)
# for i in range(0,7,2):
#     arry02[i+1][i] = 1
# print(arry02)
# #第三小题
# arry03 = np.ones((10,10))
# for i in range(1,9):
#     for j in range(1,9):
#         arry03[i][j] = 0
# print(arry03)
'''
第四题 pandas
'''
# import numpy as np
# import pandas as pd
# from pandas import Series, DataFrame
# #第一小问
# arry = np.random.randint(1,100,5)
# series01 = Series(arry)
# print(series01.index)
# print(series01.values)
# series01.index=['a','b','c','d','e']
# print(series01["e"])
# #第二小问
# dict = {
#     "语文":[98,80,60,70,56],
#     "数学":[76,89,49,69,68],
#     "英语":[93,82,96,80,79]
# }
# df = DataFrame(dict)
# Date = df.describe()
# print('各科的平局成绩如下：')
# print(Date.ix["mean"])
# print('各科的最高成绩如下：')
# print(Date.ix["max"])
# print('各科的最低成绩如下：')
# print(Date.ix["min"])
# #第三小问
# df['python'] = np.NaN
# print(df)
# df['python'] = [100,100,100,100,100]
# print(df)
'''
文件操作
'''
# import os
# def fileName(name):
#     with open(name+".txt", "a+", encoding="utf-8")as files:
#         return files
# def main():
#     name = input("请任意输入一个你的文件名：")
#     fileName(name)
#     while True:
#         content = input("请输入内容:")
#         if content == "#":
#             break
#         with open("name.txt", "a+", encoding="utf-8")as files:
#             try:
#                 files.write(content)
#                 files.seek(0)
#                 content01 = files.read()
#             except IOError:
#                 break
#     print(content01)
# main()
'''
编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
'''
def evenNum(num):
        sum = 0
        for i in range(2,num+2,2):
                sum+= 1/i
        return sum
def oddNum(num):
        sum = 0
        for i in range(1,num+1,2):
                sum+= 1/i
        return sum
def main():
        num = int(input("请输入一个数字："))
        if num%2==0:
                print(evenNum(num))
        else:
                print(oddNum(num))
main()

