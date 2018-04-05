#函数
# def 函数名(参数列表):
#     函数体

def hello():
    print('hello python3')

hello() #调用函数


#必传参数 正确的顺序
def hello1(x,y):
    print(x,y)
hello1('必传','参数')


#默认参数  给参数添加默认值  默认参数可不传
def hello3(x, y, z=100, n='june'):   #必传参数必须在前，默认参数在后
    print('x+y='+str(x+y),'z='+str(z),'n='+str(n))

hello3(100,100)
hello3(100,100,33)
hello3(100,100,33,'dddd')


#可变参数 *x  一个tuple类型
def hello4(*x):
    print(x)
hello4('s',100,True) #('s', 100, True)

#关键字参数 **y 接收到的是一个字典
def hello5(**y):
    print(y)
hello5(name='june',age=29)

#返回值 可以将一个函数作为值赋值给一个变量
def add(x,y):
    return x+y
aa = add(2,3)
print(aa)

def hello7(x,y,z):
    return x,y,z
cc = hello7(1,2,3)
print(type(cc)) #<class 'tuple'>



#全局变量 函数为变量赋值时，默认为本地变量赋值，屏蔽作用域外同名变量，使用golbal可以表示向y一个全局变量赋值
z = 10
def hello8(x):
    global z
    z = x
    print('z='+str(z))
hello8(123)