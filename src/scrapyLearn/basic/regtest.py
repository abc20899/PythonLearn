# encoding=utf8
'''
1.特殊符号
1) ^ $ * ? + {2} {2,} {2,5} |
2）[] [^] [a-z] .
3) \s \S \w \W
4) [\u4E00-\u9FA5] () \d
'''

# ^表示以什么开头 ^b 以b开头
# .表示任意字符
# *表示*前面的字符出现的次数 长度限制  >= 0
# $表示以$前面的字符结尾  3$ 表示以3结尾
# ?非贪婪匹配,按顺序匹配  默认是贪婪匹配模式，匹配到最后一个结果
# ()表示提取子字符串 括号中的字符串
# +表示+前面的字符出现大于一次的   >=1
# {2}表示前面的字符出现的次数
# {2,}表示前面的字符出现2次以上
# {2，5}表示前面的字符出现2到5次
# | 表示或关系
# [] 表示匹配括号中的任意一个字符 [abcd]  区间
# [0-9,a-z] 表示直接的字符 [.]表示. [*]表示*
# \s 表示空格一个字符长度
# \S 表示不为空格 一个字符长度
# \w 表示[a-zA-Z0-9_] 中的任意字符
# \W 表示不为上面w的的字符
# [\u4E00-\u9FA5] 表示提取中文
# \d 表示数字

import re

line = 'bobby123'
regex_str = '^b.*'  # 以b开头的任意字符串出现多次
if re.match(regex_str, line):  # match函数 参数1:模式  参数2:待匹配字符串
    print('yes')

regex_str2 = '^a'
print(re.match(regex_str2, line))  # None

regex_str3 = '.*3$'
print(re.match(regex_str3, line))  # 返回对象

regex_str4 = '^b.3$'  # 表示以b开头b后面是任意字符但是出现一次，以3结尾   bc3 bd3 等
regex_str5 = '^b.*3$'  # 表示以b开头b后面是任意字符任意长度，以3结尾   bcsss3 bsd3等

print(re.match(regex_str4, line))
print(re.match(regex_str5, line))

line2 = 'booooobby123'
regex_str6 = '.*(b.*b).*'  # 提取第一个b开头到第二个b结尾的字符串
match_obj = re.match(regex_str6, line2)  # 会贪婪匹配 匹配到最后两个bb
if match_obj:
    print(match_obj.group(1))  # group 取出所有匹配组中 第一组的字符串 返回bb  不是booooob
regex_str7 = '.*?(b.*?b).*'  # 从左边开始按顺序匹配 第一个b到第二个b结束
match_obj2 = re.match(regex_str7, line2)
if match_obj2:
    print(match_obj2.group(1))  # booooob

line3 = 'booooobbby123'
regex_str8 = '.*(b.+b).*'  # 提取以b开头，然后一个任意字符只出现大于一次的以b结尾的字符串
match_obj3 = re.match(regex_str8, line3)
if match_obj3:
    print(match_obj3.group(1))  # bbb  baab也匹配

line4 = 'booooobaab123'
regex_str9 = '.*(b.{2}b).*'
match_obj4 = re.match(regex_str9, line4)
if match_obj4:
    print(match_obj4.group(1))  # baab

line5 = 'bobby123'
regex_str10 = '(bobby|bobby123)'
match_obj5 = re.match(regex_str10, line5)
if match_obj5:
    print(match_obj5.group(1))  # bobby

regex_str11 = '([abcd].*b)'
match_obj6 = re.match(regex_str11, line5)  # bobb
if match_obj6:
    print(match_obj6.group(1))

phone = '18511697894'
regex_str12 = '1[34578][0-9]{9}'  # [0-9]0到9直接的任意字符
match_obj7 = re.match(regex_str12, phone)
if match_obj7:
    print('yes')

match_obj8 = re.match('你\s好', '你 好')
if match_obj8:
    print('yes')

hh1 = re.match('h[a-zA-Z0-9_]', 'haha_xx')  # 等同于下面
hh2 = re.match('\w', 'haha_xx')
print(hh1)
print(hh2)

study = 'study in 清华大学'
zhongwen = re.match('.*?([\u4E00-\u9FA5]+大学)', study)  # ? 非贪婪匹配
print(zhongwen.group(1))

year = '出生于2001年'
ye = re.match('.*?(\d{4})', year)
print(ye.group(1))  # 2001
