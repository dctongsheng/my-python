#-*- conding:utf-8 -*-
import time
import multiprocessing
#多进程
def work_1(f,n):
    print('work_1 start')
    for i in range(n):
        with open(f,'a') as fs:
            fs.write('i love pyhton \n')
            time.sleep(1)
    print('work_1 end')
def work_2(f,n):
    print('work_2 start')
    for i in range(n):
        with open(f,'a') as fs:
            fs.write('come on baby \n')
            time.sleep(1)
    print('work_2 end')
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=work_1,args = ('file.txt',3))
    p2 = multiprocessing.Process(target=work_2, args=('file.txt', 3))

    p1.start()
    p2.start()