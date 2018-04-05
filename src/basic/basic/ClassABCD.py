#D 继承A、B、C
class A(object):
    a = ''
    def __init__(self,a):
        self.a = a

class B(A):
    b = ''
    def __init__(self,a,b):
        super(B,self).__init__(a)
        self.b = b

class C(object): #单独继承 object类
    c = ''
    def __init__(self,c):
        self.c = c

class D(B,C):
    d = ''
    def __init__(self,a,b,c,d):
        super(D,self).__init__(a,b) #继承B 与父类参数相同
        C.__init__(self,c)   #继承C C类参数相同
        self.d = d  #自己属性


if __name__ == '__main__':
    d = D('a','b','c','d')
    print(d.d)

