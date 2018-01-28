# _*_ coding:utf-8 _*_
# import time
# print(time.altzone)
# print(time.asctime())
# print(time.clock())
# print(time.clock())
# print(time.clock())
'''
time.time()返回当前的时间戳
'''
# m = time.time()
# # print(time.ctime(m))
# n=time.localtime(m)
# print(n)
'''
time.getime()   time.local.time()返回时间元组
strftime()把时间元组转换为时间字符串
strptime（）把时间字符串转化为时间元组
mktime（）把元组转换为时间戳
sleep()推迟现成的 
'''
# print(time.strftime("%Y-%m-%d %H:%M:%S",n))
# times=time.strftime("%Y-%m-%d %H:%M:%S",n)
# print(time.strptime(times,"%Y-%m-%d %H:%M:%S"))
# print(time.mktime(n))

'''
创建一个打印当前时间的函数
'''
import time
def nowTime():
    sjc=time.time()
    sjyz=time.localtime(sjc)
    formate_time=time.strftime("%Y-%m-%d %H:%M:%S",sjyz)
    print(formate_time)
nowTime()


