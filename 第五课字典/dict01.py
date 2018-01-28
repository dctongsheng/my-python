# _*_ coding:utf-8 _*_
'''
访问字典
'''
dict01 = {"name":"xiaoming","age":"18","address":"shanghai"}
print(dict01)
print(dict01["name"])#注意通过字典的keys找对应的值用中括号
'''
修改字典
'''
dict01["address"] = "beijing"
print(dict01)
'''
添加字典
'''
dict01["hobby"] = "playing"
print(dict01)
'''
删除字典元素
del
clean清空字典
'''
del dict01["name"]
# print(dict01)
# dict01.clear()
# print(dict01)
'''
字典中的函数
len str把字典变成字符串 type 
fromkeys创建一个新字典    
get取key对应的的元素
key in dict 判断key是否在字典中
keys vaules
'''
seq = ("sex","hights")
vaule =("nan",178)
dict03 = dict.fromkeys(seq,vaule)
print(dict03)

dict02 = {"name":"xiaoming","age":18,"address":"shanghai"}
print(dict02.get('age','nan'))#如果字典有，就输出key对应原来的，没有就输出给定的
print(dict02.keys())
print(dict02.values())

'''
items将字典以元组的形式保存下来
'''
print(dict02.items())

'''
创建一个名为favorite_places的字典。在这个字典中，将三个人的名字用作键；对于其中的每个人，都存储他喜欢的1〜3个地方.
'''
donghudict_lvyou = {"zhangsan":["beijing","shanghai","guangzhou"],"lisi":["a",'b','c'],"wangwu":["xihu"]}
# name = input("请输入名字:")
# print(dict_lvyou.get(name))
print(donghudict_lvyou.items())


stu = ("www",'rrr','jjj')
print(stu[0:1])