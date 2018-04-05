import lxml
import time
from lxml import html
import requests

if __name__ == '__main__':
    text = '<span>&#x7b2c;01&#x96c6;_&#x9b4f;&#x4e66;01_&#x6b66;&#x5e1d;&#x7eaa;&#x7b2c;&#x4e00;&#x4e0a;</span>'
    print(html.fromstring(text).text)  # 第01集_魏书01_武帝纪第一上

    url = 'https://www.lrts.me/ajax/playlist/2/5901/1/next'
    response = requests.get(url)

    print(str(int(time.time())))

