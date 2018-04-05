# C继承B，B继承A
class A(object):
    a = ''
    def __init__(self,a):
        self.a = a
        print('a'+str(a))

class B(A):
    b = ''
    def __init__(self,a,b):
        super(B,self).__init__(a) #调用父类的1个参数的构造函数
        self.b = b  #子类自己的属性

class C(B):
    c = ''
    def __init__(self,a,b,c):
        super(C,self).__init__(a,b) #调用父类的2个参数的构造函数
        self.c = c #子类自己的属性

if __name__ == '__main__':
    c = C('a','b','c')
    print(c.b)

