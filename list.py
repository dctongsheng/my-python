# _*_ coding:utf-8 _*_
list01 = ['jock','xiaoming','long',['xiaohui','chenglong'],'jiajun']
# print(list01[3][1])
# list01[3][1] = "lilianjie"
# print(list01)#通过下标获取到元素，并给其赋新的值
'''
列表操作
添加元素
append往列表末尾追加元素
insert往指定位置追加元素
删除元素
pop默认删除最后一个，指定删除
del指定删除，彻底删除
remove删除指定元素，不用知道位置
查找
in
not in

# '''
list01.append('ming')
# print(list01)
list01.insert(1,"meimei")
print(list01)

list01.pop(1)
print(list01)
list01.remove("long")
print(list01)
name = "long"
print(name in list01)
name1 = 'longs'
print(name1 not in list01)
'''
列表函数，和字符串函数操作不同，传递参数的方式
len 返回列表元素的个数
max min 返回列表中的最值
count 统计指定元素在列表中出现的次数
extend 在列表后面追加一个列表，形成一个新的列表
index 查找出现的第一个位置，返回索引位置
reverse反转 sort排序 clear清空 copy复制
'''
# print(len(list01))
# print(list01.count('long'))
# list02 = ['jia','li','leng']
# list01.extend(list02)
# print(list01)
# print(list01.index('li'))
