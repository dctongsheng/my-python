# _*_ coding:utf-8 _*_
'''
del 函数名（）：
    代码
'''
# def pname():
#     print("woaini")
# pname()
'''
形参 实参
位置参数，关键字参数，默认参数，不定长参数*stars返回元组，**stars返回字典
'''

'''
可变对象和不可变对象的传递
 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict,set等则是可以修改的对象。          
'''

'''
函数的返回值
return关键字实现
'''

'''
return返回多个返回值
'''
def sun(x,y):
    return x,y
# num1,num2 = sun(1,2)
# print(num1)
# print(num2)#需要多个变量爱接收，不然的话会返回一个数组
'''
return 有什么用
返回到调用函数，后面的代码不会运行了
'''
# print(max(7,8))#返回到函数调用的地方
'''
yield 生成器
  生成一个迭代器
       ->把函数生成一个generator
       ->使用生成器可以达到延迟操作的效果，所谓延迟操作是指在需要的时候产生结果，而不是立即产生结果
         节省资源消耗，和声明一个序列不同，生成器在不使用的时候几乎是不占用内存的。
'''
def getNum(n):
    i = 0
    while i <=n:
        print(i)
        # return i
        receive=yield i     #将函数变成一个生成器generator
        print(receive)
        i+=1

# print(getNum(5))
# a = getNum(5)#把生成器赋值给一个变量
# next(a)
# a.send(888)#yeild i 为整体把888传进去，假如没有前面的next，yeild没有调用会报错

# next(a)
#使用生成器 通过next（）方法
# print(next(a))#输出yield返回的值0
# print(next(a))#在执行一次会执行直到yield为1停止

# for i in a:
#     print(i)


# a= [x for x in range(10000000)]#这样生成的一个很多数据的列表会占用很大内存
# print(a)
# a= (x for x in range(10000000))#小括号是生成器，不是元组推导式
# print(a)
# print(next(a))
# print(next(a))
# print(next(a))
'''
send
函数名.send（）   直接把send值送达yield地方
'''
# a.send(22)
# print(a.send(int(8)))


def generator():
    while True:
        receive = yield 1
        print('extra' + str(receive))


g = generator()
# print(next(g))
# print(next(g))
# print(g.send(222))
# print(next(g))
'''
递归函数：
自己调用自己
'''
#用梦境来演示递归函数

# def dream(n):
#     print("进入第%d层梦境"%n)
#     if n==3:
#         print("进入潜意识，原来我爱的人是你！开始醒来")
#     else:
#         dream(n+1)
#     print("从第%d层梦境中醒来"%n)
# dream(1)
'''阶乘
'''
def jiecheng(n):
    if n==1:
        return 1
    else:
        return n*jiecheng(n-1)
# print(jiecheng(6))
'''
费布那切数列
'''
def fibo(n):
    if n==0 or n==1:
        return 1
    else:
        return(fibo(n-1)+fibo(n-2))
# print(fibo(5))
# i = 2
# print("1 1",end=" ")
# while i<20:
#     print(fibo(i),end=" ")
#     i+=1
'''
lamada 参数 ： 表达式
默认会返回
不放for 和if（特殊情况下可以）
'''
s = lambda :"我是小猪"  #声明一个匿名函数并且赋值给s
print(s())              #通过s调用
num = lambda x:x**2
print(num(5))
num02 = lambda x,y:x*y
# #三元运算符：条件成立的内容  if  条件   else  条件不成立的内容
num03 = lambda x,y:x if x>2 else y
print(num03(3,5))
'''字典排序sort函数只适用于list
**list.sort()是对象操作，没有返回值，直接在其基础上修改
而sorted（）是内置函数，有返回值，返回一个列表，必须用变量名来接收
'''
dict = {'a':1,'c':2,'b':3}
list = sorted(dict)
print(list)
dict = sorted(dict.items(),key=lambda x:x[0],reverse=True)#默认用key排序，可以自己定义,加入lamda，可指定元组的元素
#key=lambda x:x[1]中的x指的是列表中的每一个元素，
print(dict)#
print({k:v for k,v in dict})
#字典列表的排序
dict02 = [{"name":"joe","age":18},
          {"name":"long","age":8},
          {"name":"cnn","age":28}]
dict02 = sorted(dict02,key=lambda x:x["age"],reverse=True)
print(dict02[1])
'''
高阶函数
map（函数，一个或多个序列）做映射，返回一个map对象,然后对map对象操作就行了
fitter类似于map只是对序列进行过滤
reduce所有元素进行函数操作，进行数据合并
'''
list01 = [1,2,3,4,5]
newlist=map(lambda x:x**2,list01)
# print(list(newlist))
# list(newlist)
# print(list(newlist))
# #再加个列表的话
list02 =[4,5,6,7,8]
# newlist01=map(lambda x,y:x*y,list01,list02)
# print(list(newlist01))

newlist02 = filter(lambda x:x>5,list02)
print(list(newlist02))
from functools import reduce
newlist03 = reduce(lambda x,y:x+y,list02,1)#可以设置初始值放到最后
print(newlist03)

 #练习：
# name=["long","joe","mei",'gege']
# age=[23,44,2,12]
# sex=['m','w','m','w']
#  # 案例一：格式化用户的英文名，要求首字母大小，其它字母小写
# newName=map(lambda x:x.title(),name)
# print(list(newName))
#  # 案例二：将用户英文名、年龄、性别三个集合的数据结合到一起，形成一个集合
# newjihe=map(lambda x,y,z:(x,y,z),name,age,sex)
# newjihe=list(newjihe)
# print(list(newjihe))
#  # 案例三：过滤性别为男的用户
# newjihe1=filter(lambda x:x[2]=="m",newjihe)
# print(list(newjihe1))
#  # 案例四：求性别为男的用户的平均年龄
# newage=reduce(lambda x,y:x+y[1],newjihe,0)
# print(newage/len(newjihe))



