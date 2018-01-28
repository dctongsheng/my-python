# _*_ coding:utf-8 _*_
try:
    open("aaa.txt","r",encoding="utf-8")
except Exception as e:#有异常时候执行，没有异常执行下面的else
    print(e)
else:                   #没有异常执行的代码块
    print("ok")
finally:                #都要执行的代码块
    print("good")