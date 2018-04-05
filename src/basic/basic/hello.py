#coding=utf-8

'''
语法简洁、优雅、灵活、相较于c、c++、java运行效率慢
动态、面向对象
x,y = y,x  交换两个变量等
应用：
爬虫 Scrapy
AI机器学习 Tensor Flow
自动化运维测试、
大数据 Spark
web开发 Flask、Django
脚本处理
'''

print("hello world")
print(1+3)
print("hello","junechiu")
print('i am %s' % 'junechiu')  #占位符

#input函数
name = input()
print('你好',name)
name = input('请输入名字')
print('你好',name)

#exit() 退出python

#变量不需要声明类型，但是必须要赋值

#整形类型
a = 100
#浮点类型
pi = 3.14
#字符串
s = 'hehe'
print(a,pi,s)

#多个变量赋值
a = b = c = 200
print(a,b,c)

#多元赋值
x,y,z = 100,200,'dddd'
print(x,y,z)

#查询变量类型 type
aa = 1000
print(type(aa)) #<class 'int'>
print(isinstance(aa,int))  #True


a = 11
b = int(0b1011)
if a >= b:
 print('yes')
else:
 print('no')

t = (1,2,'b','b')
if 2 in t:
 print('2')
else:
 print('0')

