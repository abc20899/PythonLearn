#单继承  super函数 父类必须继承object类
class Persion(object):
    name = ''
    age = 0
    __sex = '' #私有变量

    #构造函数
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.__sex = sex
    #函数
    def set_sex(self,sex):
        self.__sex = sex

    def get_sex(self):
        return self.__sex

#单继承
class Student(Persion): #继承Persion
    persion_id = 0  #子类属性

    #定义构造方法
    def __init__(self,name,age,sex,persion_id):
        # 调用父类的构造方法
       # Persion.__init__(self,name,age,sex)
       super(Student,self).__init__(name,age,sex) #调用父类的init
       self.persion_id = persion_id

    #重写父类的方法
    def set_sex(self,sex):
        self.__sex = sex

    def get_sex(self):
        return self.__sex


if __name__ == '__main__':
      # 单继承
   student = Student('june',29,'男',10010)
   print(student.age)
