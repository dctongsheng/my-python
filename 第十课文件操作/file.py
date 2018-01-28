# _*_ coding:utf-8 _*_、
#打开文件
# file01=open("python.txt",'r',encoding="utf-8")
# print(file01)#编码为cp936，如果要修改在后面加上encoding=utf—8
# file01.close()
#读取文件read
#readlines  一次性读完，每行保存在列表中
# content=file01.read()
# print(content)
# file01.close
#with open(_) as   不在用close关闭文件  配合for lines 输出每一行
# with open("python.txt",'r',encoding="utf-8") as file02:
#     # content = file02.read()
#     # print(content)
#     i = 1
#     for lines in file02:
#         print("这是第%d行：%s"%(i,lines))
#         i+=1

#写入write open的时候一定改变模式w
with open("python.txt",'w',encoding="utf-8") as file02:
    content = ("哈喽爱你啊")
    file02.write(content)
#函数，tell    seek（）0,1,2, 指针操作