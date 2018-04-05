import re

download_dict = dict()
download_dict['title'] = 'dddd'
download_dict['url'] = 'http://ssss.com/mp4'

arr = []
arr.append(download_dict)

strss = '[{"url": "http://i.meizitu.net/2018/01/21c01.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c02.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c03.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c04.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c05.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c06.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c07.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c08.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c09.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c10.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c11.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c12.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c13.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c14.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c15.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c16.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c17.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c18.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c19.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c20.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c21.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c22.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c23.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c24.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c25.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c26.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c27.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c28.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c29.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c30.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c31.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c32.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c33.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c34.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c35.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c36.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c37.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c38.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c39.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c40.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c41.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c42.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c43.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c44.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c45.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c46.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c47.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c48.jpg"}, {"url": "http://i.meizitu.net/2018/01/21c49.jpg"}]'


def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title

if __name__ == '__main__':
    sss = '💌呆奶💞 -锄禾日当午，汗滴禾下土『快手互粉有没有PSY318647094』'
    zhongwen = re.match('.*?([\u4E00-\u9FA5].*)', sss)  # ? 非贪婪匹配
    print(zhongwen.group(1))