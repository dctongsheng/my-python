# _*_ coding:utf-8 _*_
'''
先看列表或者是字典是否大于等于二维，如果大于二维，必须弄清楚，把用的数据进行深复制
'''
import copy
list01 = [1,2,[3,4]]
list02 = list01[:]
list03 = copy.deepcopy(list01)
print(list01)
print(list02)
print(id(list01))
print(id(list02))
list01[1] = 100
print(id(list01[0]))
print(id(list02[0]))

list01[2][1] = 100
print(list01)
print(list02)#二维里面的数也变了，证明只是copy了表面
print(list03)#深度copy，无论怎么变都与我无关了