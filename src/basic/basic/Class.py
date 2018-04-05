#class 定义一个类   _class内部使用  _Persion
# class 类名(父类):
#单下划线 protected 保护类型 只允许本类和子类访问  不能用于 from module import*

class Persion:
    pass

class Persion(object): #object是最终的父类  本类的父类
    pass

class Persion2:
    #定义属性
    name = 'june'
    age = 29
    __sex =''  #__两个下划线表示私有属性，私有方法也是如此，不能被外部类所访问

    #定义构造方法
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.__sex = sex

    #类方法
    def getSex(self):
        return self.__sex

    def setSex(self,sex):
        self.__sex = sex

#调用  main 方法
if __name__ == '__main__':
    persion = Persion2('june',29,'男') #实例化Persion2对象
    persion.age = 20 #修改属性
print(persion.name,persion.age,persion.getSex())  #june 29 男
