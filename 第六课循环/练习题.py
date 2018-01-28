# _*_ coding:utf-8 _*_
'''
把乘法表打印出来%d"*"%d"="%d%(j,i,j*i)
'''
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d"%(j,i,j*i),end=" ")#格式化输出应该引号中
#     print("\n")

# i = 1
# while i<10:
#     j = 1
#     while j<=i:
#         print("%d*%d=%d"%(j,i,i*j),end = " ")
#         j+=1
#     i+=1
#     print()
i = 1
# while i<10:
#     for j in range(1,i+1):
#         print("%d*%d=%d"%(j,i,i*j),end = " ")
#     i+=1
#     print()
'''
求和
'''
# sum = 0
# for i in range(1,101):
#     sum+=i
#     print(sum)
# print(sum)
'''
输入字符串，把字符串变成大写以列表的形式输出，没看清题目
'''
# str01 = str(input("请输入字符串："))
# str02 = str01.upper()
# print(str02)
# list01 = []
# list01.append(str02)#列表操作直接会生成新的列表
# print(list01)

# str01 = input("请输入字母或则数字：")
# list01 = []
# for i in str01:
#     if i.isdecimal() == True:
#         list01.append(int(i))         #列表的append操作，直接往里面加元素
#     else:
#         list01.append(i.upper())
# print(list01)
'''
打印所有的水仙花数
'''
# for i in range(0,10):
#
#     for j in range(0,10):
#
#         for k in range(1,10):
#             if k*100+j*10+i == k**3+j**3+i**3:
#                 print(k,j,i)
'''
老师的方法
'''
# for m in range(100,1000):
#     x = m//100
#     y = m%100//10
#     z = m%100%10
#     if x*100+y*10+z == x**3+y**3+z**3:
#         k = x*100+y*10+z
#         print(k)

'''
打印菱形 
'''
for i in range(1,8,2):
    print(("*"*i).center(9))
    if i==7:
        for i in range(5,0,-2):
            print(("*"*i).center(9))
'''
求矩阵对角线之和
'''
# m = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# s = 0
# k = 0
# for i in range(3):
#     s+=m[i][i]
#     k+=m[i][2-i]     #注意找对角线的下标规律
#
# print(s,k)
'''
给一组数字，能组成多少互不相同的数字
'''
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i !=j and j!=k and k!=i:
#                 print(i,j,k)
# num = [i*100+j*10+k for i in range(1,5) for j in range(1,5) for k in range(1,5) if i !=j and j!=k and k!=i]
# print(num)