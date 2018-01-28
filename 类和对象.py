# _*_ coding:utf-8 _*_
'''
类和对象
'''
#创建一个类  类属性，实例属性 类方法
# 实例属性中的__inint__为构造方法，构造方法不需要调用，在实例化的时候自动调用
# 实例属性通过构造方法来实现
#
# 类属性 又叫类变量，在类里面，构造方法之外，调用通过 类名.属性名使用
#内置类函数有__dict__,字典包括属性名和值  __doc__,文档  __bases__
#私有属性，双下划线开头声明，不能直接访问，可以通过预留接口访问（就是创建函数）

#类方法@classmethod   cls
#静态方法 加@staicmethod 不能访问实例属性
#通过类名的方式调用
class person():
    #类文档说明：这是以人为对象创建的类
    count = "中国"#类属性
    def __init__(self,name,age,sex,personnum=0):
        self.name=name          #通过self创建实例属性，并且赋值
        self.age=age
        self.__sex=sex#私有属性
        self.personnum=personnum
    def introdion(self):        #self不是关键字，代表的是当前对象
        print("我是%s，我今年%s岁了"%(self.name,self.age))#在方法里面使用实例属性
    #累加
    def addperson(self):
        self.personnum+=1
        print("一共有%d个人"%self.personnum)
    @staticmethod
    def aa():
        print("我来自%s"%person.count)
person1=person("joe",18,"m")
person1.aa()

person1.introdion()
person1.addperson()
person1.addperson()
person2=person("joe",18,"m")


#访问属性 通过对象名.属性名
# print(person1.count)
'''
通过内置函数来访问属性
getattr(obj, name[, default]) : 访问对象的属性
hasattr(obj,name) : 检查是否存在一个属性
setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性
delattr(obj, name) : 删除属性
'''
# print(hasattr(person1,"sex"))
# print(person1.__dict__)
'''
继承和多态
子类继承父类通过super来继承父类的实例属性  或者用父类名.__init__
'''
class animal():
    def __init__(self,name,food):
        self.name=name
        self.food=food
    def eat(self):
        print("%s爱吃%s"%(self.name,self.food))
class dog(animal):
    def __init__(self,name,food,drink):
        super().__init__(name,food)
        self.drink=drink
    def drinks(self):
        print("%s爱喝%s"%(self.name,self.drink))
dog1=dog("金毛","骨头","可乐")
dog1.eat()
dog1.drinks()#参数名最好和方法名字不一样
