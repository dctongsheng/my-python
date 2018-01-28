# _*_ coding:utf-8 _*_
'''
单线程
'''
import time
import threading

# def music(name,loop):
#     for i in range (loop):
#         print("listen music %s %s"%(name,time.ctime()))
#         time.sleep(2)
# def moive(name,loop):
#     for i in range (loop):
#         print("look moive %s %s"%(name,time.ctime()))
#         time.sleep(2)
# if __name__=="__main__":
#     music("平凡之路",3)
#     moive("一千零一夜",4)
#     print(time.ctime())
'''
多线程，运用threading模块
'''
# def music(name,loop):
#     for i in range (loop):
#         print("listen music %s %s %s"%(name,time.ctime(),threading.Thread.getName(t1)))
#         time.sleep(1)
# def moive(name,loop):
#     for i in range (loop):
#         print("look moive %s %s %s"%(name,time.ctime(),threading.Thread.getName(t2)))
#         time.sleep(1)
# t1 = threading.Thread(target=music,args=("平凡之路",3))
# t1.setName("musicThread")
# t2 = threading.Thread(target=moive,args=("一千零一夜",3),name="moiveThread")
# if __name__=="__main__":
# #4.守护主线程，当主线程执行完毕会杀死子线程
#     t1.setDaemon(True)
#     t2.setDaemon(True)
#     t1.start()
#     t2.start()
# #什么是主线程和子线程
#     # threading.Thread.join(t1)#3.让主线程在最后执行，阻止多线程或者t1.join
#     print("我是主线程")
#     # print(t1.ident)
'''
给多线程加锁
'''
balance = 0
def change(n):
    global balance
    balance+=n
    balance-=n
#获得线程锁
lock = threading.Lock()
def run_thread(n):
    for i in range(1000000):
        #获得锁
        lock.acquire()
        try:
            change(n)
        finally:
            #释放锁
            lock.release()
t1=threading.Thread(target=run_thread,args=(4,))
t2=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)#每次结果都会改变，需要加锁