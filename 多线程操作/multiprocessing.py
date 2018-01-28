# _*_ coding:utf-8 _*_
import time
import multiprocessing
#单进程
# def work_1(f,n):
#     print("work_1 start")
#     for i in range(n):
#         with open(f,"a",encoding="utf-8") as fs:
#             fs.write("i love you\n")
#             time.sleep(1)
#     print("work_1 end")
# def work_2(f,n):
#     print("work_2 start")
#     for i in range(n):
#         with open(f,"a",encoding="utf-8") as fs:
#             fs.write("baby baby\n")
#             time.sleep(1)
#     print("work_2 end")
# if __name__=="__main__":
#     work_1("file.txt",3)
#     work_2("file.txt",2)
#多进程
def work_1(f,n):
    print("work_1 start")
    for i in range(n):
        with open(f,"a",encoding="utf-8") as fs:
            fs.write("i love you\n")
            time.sleep(1)
    print("work_1 end")
def work_2(f,n):
    print("work_2 start")
    for i in range(n):
        with open(f,"a",encoding="utf-8") as fs:
            fs.write("baby baby\n")
            time.sleep(1)
    print("work_2 end")
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=work_1,args = ('file.txt',3))
    p2 = multiprocessing.Process(target=work_2, args=('file.txt', 3))
    p1.start()
    p2.start()