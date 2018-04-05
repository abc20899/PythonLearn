#6种标准类型
# Number 数字
# String 字符串
# List  列表
# Tuple 元组
# Dictionary 字典
# Sets 集合

# int float bool complex
a = 100
b = 100.00
c = True
print(a,b,c)

#complex(x,y) x实部y虚部
x = 1.2
y = 2.3
z = complex(x,y)
print(z) #(1.2+2.3j)  a + bj

print(9/4)   #2.25
print(9//4)  #2
print(2**3)  #8


#字符串用单引号或者双引号 用\作转义
name = 'I\'m junechiu'
print(name)
print(len(name)) #输出字符串的长度
print(name[0]) #输出第一个字符
print(name[0:-1]) #输出第一个到倒数第二个
print(name[1:2])  #输出1到2个字符
print(name[2:]) #输出2以后的字符串
print(name*2) #输出2次
print('Hello,'+name) #拼接
print('june' in name) #是否包含
print('june' not in name)
print(name.upper())  #转换成大写
print(name.lower()) #转换成小写
print(name.capitalize()) #字符串第一个字符大写
print(name.isspace()) #是否包含空格
print(name.replace('june','hehe')) #替换操作
print("h*h*".split("*"))#分割操作
print(name.strip()) #去掉字符串的左右空格
print(name.lstrip()) #去掉左空格
print(name.rstrip()) #去掉右空格


#占位符 %d %f %s
hehe = 'hello,%s' % 'python'
print(hehe)
aaa = 'python %d %s %.2f' % (666,'niubai',9.99)
print(aaa)

sss = ''' 
ssss\n
hahah\n
随便写\t
呵呵\t
'''
print(sss)


##列表 中可以添加不同类型的元素
arr = ['hehe',100,100.00,True,'$aa']
print(arr)
print(len(arr)) #长度
#访问元素
print(arr[2]) #下标为2的元素
print(arr[2:])#输出2以后的元素
print(arr[2:4]) #输出下标2到4的元素
#添加元素
s1 = [False]
arr = arr+s1 #连接元素
print(arr)
s2 = [200,44]
arr.extend(s2) #在列表的末尾追加一个列表
print(arr)
arr.append("哈哈") #末尾拼接一个新的对象
print(arr)
arr.insert(2,"插入") #在指定位置插入一个元素
print('拼接打印：'+str(arr))
#更新元素
arr[1] = '更新第二个元素'
print('更新：'+str(arr))
#删除元素
arr.pop() #默认删除最后一个元素
arr.pop(1) #删除第二个元素
del arr[3] #删除指定位置
arr.remove('$aa') #删除匹配对象
print(arr)
#其他方法
print(arr*2) #打印两次
arr.reverse() #反向列表
arr2 = arr.copy() #复制列表
print(arr2)
arr2.clear() #清空列表
print(arr2)



#元组  用()包含元素 元素不能被修改 可以包含一个list类型的元素
arrInner = [100,22,'ddd']
array = (100,100.00,'arr',True,'$$%^',arrInner)
print(array) #(100, 100.0, 'arr', True, '$$%^', [100, 22, 'ddd'])
print(array[2:])
array2 = (1,False) #单独的一个bool 类型的元素不能加入元祖
print(array+array2) #(100, 100.0, 'arr', True, '$$%^', [100, 22, 'ddd'], 1, False)



#字典 key必须唯一，类型为不可变类型 {}创建空字典  dict()方法创建一个字典  key-value无序的
persion = {'name':'junechiu','age':29,'job':'coder'}
print(persion)
print(persion['name']) #根据key输出value
#修改元素
persion['age'] = 30
print(persion)
#新增元素
persion['id'] = 10010
print(persion)
#删除元素 pop('id')
#清空元素 clear
#dict()方法创建一个字典
d = dict(id=10010,des='i am junechiu',job='coder')
print(d)
print(d.keys()) #输出所有key
print(d.values()) #输出所有value



#sets集合 无序不重复的序列，用{}或者set()创建
s3 = {'name':'june','age':12}
print(s3)
s4 = set()
s4.add('i')
s4.add('am')
s4.add('june')
print(s4) #{'june', 'i', 'am'}



#python 空值用 None 来表示
#数据类型转换 内置一些函数
x = '22'
cc = int(x) #转换为int
print(cc)
cc = float(x)
print(cc)
cc = str(x)
print(cc)
cc = list(x) #转换为一个列表
print(cc) #['2', '2']


len_num = len([1,2,3,4,5,6])  #长度
print(len_num)
max_int = max([1,2,3,4,5,6,8]) #最大值
print(max_int)
min_int = min((1,2,3,4,5))
print(min_int)
max_char = max('hello world')
print(str(max_char))
min_char = min('hello world')
print(min_char)  #空格最前

set_num = {1,2,3}
print(len(set_num))
b = 1 in set_num
print(b)
set_all = {1, 2, 3, 4, 5, 6}
set_1 = {2, 3}
set_2 = set_all - set_1  # 两个集合的差集
print(set_2)
set_3 = {4,5}
set_result = set_all & set_3  #两个集合的交集
print(set_result)
set_00 = {1, 2, 3, 4, 5}
set_11 = {1, 3, 4, 8, 9}
set_22 = set_00 | set_11  # 合并两个集合并且元素不重复
print(set_22)

set_lan = set()
set_lan.add('python')
set_lan.add('java')
set_lan.add('c++')
print(set_lan)

handle = {'W':'前','A':'左','D':'右','S':'后'}
print(handle['W'])
handle['W'] = '向前'   #修改值
print(handle)


a = 'hello'
print(id(a))
a = a + ' python'         #一个新的字符串
print(a)
print(id(a))              #打印a的内存地址


aa = [1,2,3]
print(hex(id(aa)))
bb = aa
print(hex(id(bb)))