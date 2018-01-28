# _*_ coding:utf-8 _*_
#在当前脚本运行
#输出__main__
def a():
    print("我是a方法")
if __name__ =="__main__":#为了防止函数a，此文件被别的地方调用的时候执行，
    a()
    print(__name__)