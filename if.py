# _*_ coding:utf-8 _*_
#比较三个数的大小
# a = int(input("请输入第一个数字："))
# b = int(input("请输入第一个数字："))
# c = int(input("请输入第一个数字："))
# if a>b:                               #注意if语句的缩进，
#     if a>c:
#         print("最大的数是%d"%a)       #注意没有逗号
#     else:
#         prient("最大的数是%d"%c)
# elif b>c:
#         print("最大的数是%d"%b)
# else:
#         print("最大的数是%d"%c)

'''
猜拳游戏
注意一定得区分英文和汉子得冒号
'''
import random
user = str(input("请输入剪刀 石头 布 任意一个："))
cont = ["剪刀","石头","布"]
num = random.randint(0,2)
if user == "剪刀":
    if cont[num] == "剪刀":
        print("电脑输入的是%s 平局"%cont[num])
    elif cont[num] =="石头":
        print("电脑输入的是%s 你输了"%cont[num])
    else:
        print("电脑输入的是%s 你赢了了"%cont[num])
elif user == "布":
    if cont[num] == "剪刀":
        print("电脑输入的是%s 你输了"%cont[num])
    elif cont[num] =="石头":
        print("电脑输入的是%s 你赢了"%cont[num])
    else:
        print("电脑输入的是%s 平局"%cont[num])
elif user == "石头":
    if cont[num] == "剪刀":
        print("电脑输入的是%s 你赢了"%cont[num])
    elif cont[num] =="石头":
        print("电脑输入的是%s 平局"%cont[num])
    else:
        print("电脑输入的是%s 你输了"%cont[num])
else:
    print("你输入的有误")



