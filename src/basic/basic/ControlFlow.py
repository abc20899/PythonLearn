#控制流程 和java 差不多   每个条件后面需要加冒号:  用elif代替else if  没有switch case   使用缩进划分语句块

week = 1
if week == 1:
    print("星期一")
if week == 2:
    print("星期二")
if week == 3:
    print("星期三")
if week == 4:
    print("星期四")
if week == 5:
    print("星期五")
if week == 6:
    print("星期六")
if week == 7:
    print("星期日")

#循环语句 加冒号
strList = ['s1','s2','s3','s4','s5']
for s in strList:
    print(s) #s1 s2 s3 s4 s5

#while 语句  中可以有else
m = 5
n = 0
while n<=5:
    n+=1
    print('循环次数'+str(n))
else:
    print('不符合条件')

#break 跳出循环体  continue中断此次循环，继续下一轮循环

#pass 是空语句 不做任何事情  为了保持程序结构的完整性
pass

