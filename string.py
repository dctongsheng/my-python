# _*_ coding:utf-8 _*_
'''
格式化输出 %d  %f   %s
'''
# name = "小伟"
# ge = 18
# a = '北京'
# print('我叫%s,我今年%d了，我住在%s'%(name,ge,a))   #注意一定要用逗号隔开
'''
常用字符串函数find index count repleace split capitalize title lower upper
'''
#find
str = 'i love python oo'
# print(str.find('o'))#返回的是该字符串的位置，注意引号
# print(str.find('w'))

#index
# print(str.index('o'))
# print(str.index('w'))#如果没有会报错

#count
print(str.count('o'))
print(str.count('o',2,5))#指定位置查找,返回该元素的出现的次数
#
# #replace
# print(str.replace('o','O',1))#后面的数字为替换的次数

#split
print(str.split(" ",1))#返回一个列表     #1为maxsplit表示分割为几个字符串


#capitalize upper
print(str.capitalize())#把字符串的首字母大写
print(str.upper())

#title
print(str.title())#每个单词的首字母大写

#startswith endswith
print(str.startswith('i'))#返回bool


#ljust rjust center   左对齐 右对齐 居中
#lstrip rstrip strip  去除空格

#partition 分割三部分 左边 自己 右边
print(str.partition('love'))#返回一个元组
#join 每个字母后面插入str1，返回一个新的字符串
str1 = " "
list = ["meizi","love","me"]
print(str1.join(list))

# isspace isalnum isdigit isalpha  判断空格 字母或数字 数字 字母
print(str.isalnum())