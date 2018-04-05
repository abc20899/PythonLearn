print('please input your name')
account_list = ('john','lisa','june')
user_name = input()
print('please input your password')
user_passwd = input()
if user_name in account_list:
 if user_passwd == '123456':
    print('welcome')
 else:
    print('password is wrong')
else:
 print('sorry')


counter = 1
while counter <= 10:
  counter+=1
  print(counter)

t = (1,2,3,4,5)
for a in t:
 print(a)

a = [['a','b','c','d'],(1,2,3)]
for x in a:
  for y in x:
    print(y)

tt = [1,2,3]
for c in tt:
  if c == 2:
    continue    #跳过此条件的执行
  print(c)

arr = set()
for i in range(0,10):
    arr.add(i)
print(arr)


for x in range(0,10,2):
    print(x,end=' | ')

for x in range(10,0,-2):  #步长为-2
    print(x,end=' | ')


a = [1,2,3,4,5,6,7,8,9]
b = a[0:len(a):2]    # 步长为2
print(b)

#返回多个值
def result(x,y):
    a = x*3
    b = y*2+10
    return a,b

su = result(2,3)
print(su)
#(6, 16)

a,b,c = 1,2,3
d = 1,2,3
print(type(d))


class Student():
   name = ''
   age = 0
   score_dic = {}

   # 构造函数 实例化时自动调用
   def __init__(self, name, age, score_dic):
       self.name = name
       self.age = age
       self.score_dic = score_dic

   def info(self):
      print(self.name +' '+ str(self.age) + ' score:' + str(self.score_dic))
stu = Student('小明',12,{'Math':99})
stu.info()
print(stu.__dict__)


class Person(object):
    sum = 0  # 类变量

    def __init__(self):
        self.__class__.sum += 1  # 调用类变量
        print('Person: sum' + str(self.__class__.sum))

    # 定义一个类方法
    @classmethod  # 装饰器
    def print_sum(cls):
        print('sum:' + str(cls.sum))

    # 定义一个静态方法
    @staticmethod
    def add():
        print('static')

p1 = Person()
p2 = Person()
p3 = Person()
Person.print_sum()
Person.add()