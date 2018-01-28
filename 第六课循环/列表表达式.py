# _*_ coding:utf-8 _*_
#字典的列表表达式
'''
enumerate :
用法：对于可迭代对象，可以同时得到它的索引和值
可以跟参数，参数表示索引的起始值
'''
list01 = ['beijing ','tiananmrn','changcheng']
print(list(enumerate(list01,2)))
for index,item in enumerate(list01,1):#
    print(index,item)
'''
列表表达式如下
能把列表变成字典的形式，
'''
dict01 = {index:item for index,item in enumerate(list01,1)}
print(dict01)
'''
items,把字典转拆分，
'''
print(dict01.items())
for k , v in dict01.items():
    print(k)
list02 = [v for k , v in dict01.items()]
print(list02)
'''
嵌套列表推导
二维的。
'''
list03 = [['liming','joe','long','leilei'],['zhu','niniu','q','meimei']]
# list04 = []
# for i in list03:
#     for n in i:
#         list04.append(n)
# print(list04)
list04 = [n.capitalize() for i in list03  for n in i if len(n)<4]
print(list04)

