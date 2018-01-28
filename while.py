# _*_ coding:utf-8 _*_
'''
while条件表达式：      #当条件为真时，执行循环
    要执行得代码       #执行完之后，回到条件表达式
'''
# i = 1                #初始化
# while i <= 5:
#     print("i love you")
#     i += 1
'''
求和1-100
'''
i = 1#初始化一个变量
num = 0
while i<=100:
    num += i
    i += 1
print(num)
'''
总结：while可以利用条件重复做一件事情
'''

'''
while嵌套
'''
# i = 1
# while i<=5:
#     str ="*"*i
#     print(str.center(100," "))
#     i+=1
i = 0
while i<5:                  #定义五行
    m = 0
    while m<=i:             #控制个数
        print("*",end=" ")  #print的结束为空格，默认为换行
        m+=1                #每行星星的个数
    i+=1
    print()                 #执行完内部循环，换行
'''
while 条件：
    #条件成立的时候执行的代码
else：
    #条件成立执行的代码
'''
# a = 0                   #初始化一个变量
# while a<5:
#     print("爱你一万年")
#     a+=1                #累加
# else:                   #条件不成立时候
#     print("我是至尊宝")

'''
跳转语句
break：终止循环，无论条件是否为真，
'''
a = 0                   #初始化一个变量
while a<5:
    if a==3:
        print("紫霞仙子：我爱你")
        break
    print("至尊宝：爱你一万年")
    a+=1                #累加
'''
例子1
'''
# m = input("是否退出程序n/y:")
# while m=="n":
#     if m=="y":
#         print("已经退出程序，谢谢使用")
#         break
#     print(m)
'''
以上代码没法实现那个功能，必须把input放到while里面才行
'''
# while True:
#     flag = input("是否退出程序n/y:")
#     if flag =="n":
#         pass
#     else:
#         print("已经退出程序，谢谢使用")
#         break
'''
老师的代码
'''
while True:
    flag = input("是否退出程序n/y:")
    print(flag)
    if flag == "y":
        print("已经退出程序，谢谢使用")
        break
'''
continue
跳出当前循环，执行下一循环
'''
a = 0
while a<10:
    a+=1
    print("现在是第%d圈"%a)
    if a == 5:
        print("趁老师没注意，直接跑第下一圈吧")
        continue
    print("好累啊")
