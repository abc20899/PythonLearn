# # encoding=utf8
# import random
#
# import requests
# from bs4 import BeautifulSoup
# import lxml
# from selenium import webdriver
# from selenium.webdriver import DesiredCapabilities
#
# from src.fir.agent import USER_AGENTS
#
#
# def getall():
#     url = 'http://www.mzitu.com/all/'
#     response = requests.get(url)
#     # print(response.text)
#     soup = BeautifulSoup(response.text, 'lxml')
#     all_a = soup.find('div', class_='all').find_all('a')
#     for a in all_a:
#         print(a)
#
#
# def ysts8():
#     base_url = 'http://www.ysts8.com'
#     single_url = 'http://www.ysts8.com/play_10164_46_1_5.html'
#     response = requests.get(single_url)
#     soup = BeautifulSoup(response.text, 'lxml')
#     mp3url = base_url + soup.find('iframe')['src']
#     response = requests.get(mp3url)
#     # requests.utils.get_encodings_from_content(response.text)
#     response.encoding = 'gb2312'  # 知道编码
#     print(response.text)
#
#
# # https://cuiqingcai.com/2599.html
# # 下载chromedriver放到 /usr/local/bin
# # 下载http://phantomjs.org/  phantomjs拷贝到/usr/local/bin
# # 配置环境变量 export PATH=${PATH}:/usr/local/bin
# def test_selenium():
#     path = "/usr/local/bin/chromedriver"  # chromedriver完整路径，path是重点
#     browser = webdriver.Chrome()
#     browser.get('http://www.python.org')
#     print(browser.title)
#     print(browser.page_source)
#     browser.save_screenshot('python.png')  # 保存图片
#
#
# def youshengjs():
#     url = 'http://www.ysts8.com/play/flw.asp?url=%B5%A5%CC%EF%B7%BC%2F%B7%E2%C9%F1%D1%DD%D2%E5%28%B5%E7%CA%D3%B0%E6%29180%BB%D8%2F003%2Emp3&jiidx=/play%5F10164%5F46%5F1%5F4%2Ehtml&jiids=/play%5F10164%5F46%5F1%5F2%2Ehtml&id=10164&ji=3&said=46'
#     dcap = dict(DesiredCapabilities.PHANTOMJS)
#     # 从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
#     # 设置全屏,调用启动的浏览器不是全屏的，有时候会影响某些操作
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--headless')
#     # 设置页面完全加载的超时时间，完全加载即完全渲染完成，同步和异步脚本都执行完
#     browser = webdriver.Chrome(chrome_options=chrome_options)
#     browser.set_page_load_timeout(10)
#     # 隐性等待设置为10秒
#     browser.implicitly_wait(5)
#     browser.get(url)
#     print(browser.page_source)
#
#
# if __name__ == '__main__':
#     ysts8()
