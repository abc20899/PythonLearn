import re

a = 'java|python|kotlin|ruby|javaScript'
r = re.findall('python',a)
print(r)  #返回一个列表  ['python']


b = 'strf23hj3hjf2jigh7jff8ksffih9'
r = re.findall('\d',b)  #提取所有数字
print(r)

s = 'abc,acc,asd,ade,afg,afc,ahv'
r = re.findall('a[cf]c',s)
print(r)

ss = 'A24G8D73H59D6F4G'
def convert(value):
    num = value.group()
    if int(num) >= 6:
       return '9'
    else:
       return '0'
r = re.sub('\d',convert,ss)
print(r)
#A00G9D90H09D9F0G