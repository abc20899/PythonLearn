import random
from flask import json

from bs4 import BeautifulSoup
import os

from src.spider.meizi.download import request
from src.spider.meizi.meizi_model import meizi_bean


class Meizi():

    #构造函数 传入header
    def __init__(self):
        self.user_agent_list = [
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; InfoPath.1 ',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; EasyBits GO v1.0; InfoPath.1; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729) ',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; BOLT/2.800) AppleWebKit/534.6 (KHTML, like Gecko) Version/5.0 Safari/534.6.3',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.48 Safari/525.19',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.33 Safari/530.5',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.55 Safari/534.3',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.151 Safari/534.16',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30 ChromePlus/1.6.3.1',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
            'Mozilla/5.0 (Linux; U; Android 4.0.1; ja-jp; Galaxy Nexus Build/ITL41D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Mozilla/5.0 (Linux; U; Android 4.0.3; de-de; Galaxy S II Build/GRJ22) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Mozilla/5.0 (Linux; U; Android 4.1.1; ja-jp; Galaxy Nexus Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Opera/9.80 (Android 4.0.4; Linux; Opera Mobi/ADR-1205181138; U; pl) Presto/2.10.254 Version/12.00',
            'Opera/12.02 (Android 4.1; Linux; Opera Mobi/ADR-1111101157; U; en-US) Presto/2.9.201 Version/12.02',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7; en-us) AppleWebKit/534.20.8 (KHTML, like Gecko) Version/5.1 Safari/534.20.8',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.803.0 Safari/535.1',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.794.0 Safari/535.1',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.0 Safari/534.24',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_0; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.7 Safari/533.2'
        ]
        user_agent = '''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
            Name'''
        headers = {'User-Agent': user_agent}
        self.head = headers
        self.meizi_list = []  #存储meizi_bean对象
        self.output = '/Users/junzhao/python/meiziimg/'

    #all_urls = 'http://www.mzitu.com/all/'
    def all_url(self,url):
        all_html = request.get(url,3)                #download 模块
        Soup = BeautifulSoup(all_html.text, 'lxml')  # lxml指定解析器
        all_a = Soup.find('div', class_='all').find_all('a')  # 找到class 为all的div标签，然后再找里面所有的a标签
        for a in all_a:
            title = a.get_text()
            href = a['href']

            self.update_meizi(title,href)   #更新分类

            # if 'old' not in href:                         #没有包含old
            #   if meizi_bean('',[]).query_meizi(title):    #查询是否已经爬过 如果没有爬过返回true
            #      dir_name = str(title).replace('?', '_')  # 替换？
            #      self.mkdir(dir_name)
            #      self.html(href,title)

    # 访问每一张图片连接
    def html(self,href,title):
        a_html = request.get(href,3)             #download 模块
        Soup = BeautifulSoup(a_html.text, 'lxml')
        # 获取最大页码值 倒数第二个span中保存了 最大页码值
        max_page = Soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
        urls = [] #每套图的数组 数据库
        for page in range(1, int(max_page) + 1):
            page_url = href + '/' + str(page)  # 拼接连接地址 每张图片的地址
            # print(page_url) #打印每张图片的页面连接
            imgurl = self.get_img(page_url)
            imgdic = {'url':imgurl}  #构建一个imagurl字典  数据库
            urls.append(imgdic) #将字典添加进集合  数据库
        bean = meizi_bean('',[])
        bean.insert_meizi(title,json.dumps(urls))

    # 获取真实的图片地址
    def get_img(self,pageurl):
        try:
            UA = random.choice(self.user_agent_list)
            Picreferer = {
                'User-Agent': UA,
                'Referer': 'http://i.meizitu.net'
            }
            img_html = request.get(pageurl, 3, header2=Picreferer)  # download 模块
            Soup = BeautifulSoup(img_html.text, 'lxml')
            img_url = Soup.find('div', class_='main-image').find('img')['src']
            print(img_url)  # 打印每张图片的链接
            self.saveimg(img_url)#下载图片
            return img_url  # 返回一张图片的真实地址
        except BaseException as e:
            # all_urls = 'http://www.mzitu.com/all/'
            # self.all_url(all_urls)
            print(e)
        finally:
            pass

    #根据套图名字创建文件夹
    def mkdir(self,dir_name):
        path = dir_name.strip() #去除空格
        isExists = os.path.exists(os.path.join(self.output,path))
        if not isExists:
            print(u'创建',dir_name,u'文件夹')
            os.makedirs(os.path.join(self.output,path))
            os.chdir(os.path.join(self.output,path)) #切换到此目录
            return True
        else:
            print(dir_name,u'文件夹已经存在')
            return False

    #保存图片
    def saveimg(self,img_url):
        name = img_url[-9:-4] #裁切字符串
        print(u'开始保存：',img_url)
        img = request.get(img_url,3)     #download 模块
        f = open(name+'.jpg','ab')
        f.write(img.content)
        f.close()

    #将meizi_bean添加进集合
    def add_meizi(self,meizibean):
        if meizibean is not None:
          self.meizi_list.append(meizibean)
          f = open('./meizijson.txt', 'w')  # 写模式 在当前目录下创建一个文件
          f.write(meizibean)
          f.close()

    #增加分类
    def update_meizi(self,title,href):
        if 'old' not in href:  # 没有包含old
            a_html = request.get(href, 3)              # download 模块
            Soup = BeautifulSoup(a_html.text, 'lxml')  # lxml指定解析器
            category = Soup.find('div',class_='main-meta').find('span').find('a').get_text()
            print(href+'  '+category)
            bean = meizi_bean('', [])
            if bean.query_meizi(title):
                print('数据库没有此记录')
            else:
              bean.update_meizi(title,category)

if __name__ == '__main__':
    all_urls = 'http://www.mzitu.com/all/'
    meizi = Meizi()
    meizi.all_url(all_urls)