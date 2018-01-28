# _*_ coding:utf-8 _*_

# import modles01 as mo
# print(mo.add(4,6))
# import modles2.modles3
# print(mod.addd(3,4))
#结果不是一个文件夹就不行，这时候需要导入把上一级导入当前环境
import sys
print(sys.path)
sys.path.append("..\\")
import modles2.modles3    #添加环境之后才能执行
print(modles2.modles3.addd(3,4))