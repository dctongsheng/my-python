# _*_ coding:utf-8 _*_
'''
for 变量 in 序列： #（序列可以使列表 字符串 列表元组集合，字典只能遍历keys）
      执行的代码
'''
list01 = ["jock",'long','ming','sheng']
for i in list01:
    print(i)

i = 0
while i<len(list01):
    print(list01[i])
    i+=1
'''
改进最喜欢的地点的例子
'''
favorite_places = {"ming":["dali",'beijing'],"long":["yunnan",'canghan']}
name = input("qingshurumingzi:")
for i in favorite_places:
    if i == name:
        print(favorite_places[name])
    else:
        print("shurucuowu")