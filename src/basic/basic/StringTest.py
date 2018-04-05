#字符串拼接
ok_str = ','
str_arr = ['python','java','javaScript','ruby']
print(ok_str.join(str_arr))

#字符串截取
str = '0123456789'
print(str[0:3])    #截取第一位到第三位的字符
print(str[:])      #截取字符串的全部字符
print(str[6:])     #截取第七个字符到结尾
print(str[:-3])    #截取从头开始到倒数第三个字符之前
print(str[2])      #截取第三个字符
print(str[-1])     #截取倒数第一个字符
print(str[::-1])   #创造一个与原字符串顺序相反的字符串
print(str[-3:-1])  #截取倒数第三位与倒数第一位之前的字符
print(str[-3:])    #截取倒数第三位到结尾
print(str[:-5:-3]) #逆序截取

#字符串分割
str1 = 'ab,cde,fgh,ijk'
str2 = ','
str1 = str1[str1.find(str2) + 1:]
print(str1)
#或者
s = 'ab,cde,fgh,ijk'
print(s.split(','))

#查找字符串
str1 = 'abcdefg'
str2 = 'cde'
print(str1.find(str2)) #2

#翻转字符串
str1 = 'abcdefg'
str1 = str1[::-1]
print(str1)

#扫描字符串
sStr1 = 'cekjgdklab'
sStr2 = 'gka'
nPos = -1
for c in sStr1:
    if c in sStr2:
        nPos = sStr1.index(c)
        break
print(nPos)

#比较字符串
sStr1 = 'strch'
sStr2 = 'strch'
print(sStr1 is sStr2)