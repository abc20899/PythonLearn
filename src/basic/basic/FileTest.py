#文件读取  open  read/write  close

def write_file():
    try:
        f = open('./test.txt','w') #写模式 在当前目录下创建一个文件
        f.write('hello,python')
    except BaseException as e:
        print(e)
    finally:
        if f:
           f.close()

# write_file() #调用函数

def read_file():
    try:
        f = open('./test.txt','r')
        #print(f.read()) #一次性读取所有内容
        print(f.readline()) #按行读取 返回list
    except BaseException as e:
        print(e)
    finally:
        if f:
            f.close()
#read_file()

#读取二进制文件 图片视频等
def read_byte_file():
    try:
        f = open('./jingru_8.jpg','rb')
        print(f.read())
    except BaseException as e:
        print(e)
    finally:
        if f:
            f.close()
read_byte_file()

#字符编码
# f = open("*.txt",'r',encoding='GBK',errors='ignore')