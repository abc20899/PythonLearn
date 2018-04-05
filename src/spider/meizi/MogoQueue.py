from datetime import datetime, timedelta

from pymongo import MongoClient


class MogoQueue():

    OUTSTANDING = 1  ##初始状态 等待爬取的URL

    PROCESSING = 2  ##正在下载状态 正在进行的URL

    COMPLETE = 3  ##下载完成状态 爬取完成的URL

    def __init__(self,db,collection,timeout = 300):
        self.client = MongoClient()
        self.Client = self.client(db)
        self.db = self.Client(collection)
        self.timeout = timeout

    def __bool__(self):
        """
        这个函数，我的理解是如果下面的表达为真，则整个类为真
        至于有什么用 $ne的意思是不匹配
        """
        record = self.db.find_one(
            {'status': {'$ne': self.COMPLETE}}
        )
        return True if record else False

    # 存入套图url
    def push(self, url, title):  ##这个函数用来添加新的URL进队列
        try:
            self.db.insert({'_id': url, 'status': self.OUTSTANDING, '主题': title})
            print(url, '插入队列成功')
        except BaseException as e:  ##报错则代表已经存在于队列之中了
            print(e)
            print(url, '已经存在于队列中了')
            pass

    #存入单个image url
    def push_imgurl(self, title, url):
        try:
            self.db.insert({'_id': title, 'statue': self.OUTSTANDING, 'url': url})
            print('图片地址插入成功')
        except BaseException as e:
            print(e)
            print('地址已经存在了')
            pass

    #修改状态将就绪状态 改为 处理状态并存入当前时间戳 || 取出就绪状态
    def pop(self):
        """
        这个函数会查询队列中的所有状态为OUTSTANDING的值，
        更改状态，（query后面是查询）（update后面是更新）
        并返回_id（就是我们的ＵＲＬ）
        如果没有OUTSTANDING的值则调用repair()函数重置所有超时的状态为OUTSTANDING，
        $set是设置的意思，和MySQL的set语法一个意思
        """
        record = self.db.find_and_modify(
            query={'status': self.OUTSTANDING},
            update={'$set': {'status': self.PROCESSING, 'timestamp': datetime.now()}}
        )
        if record:
            return record['_id']
        else:
            self.repair()
            raise KeyError

    #返回套图名称
    def pop_title(self, url):
        record = self.db.find_one({'_id': url})
        return record['主题']

    #取出就绪状态的 记录
    def peek(self):
        """这个函数是取出状态为 OUTSTANDING的文档并返回_id(URL)"""
        record = self.db.find_one({'status': self.OUTSTANDING})
        if record:
            return record['_id']

    #更新记录为完成状态
    def complete(self, url):
        """这个函数是更新已完成的URL完成"""
        self.db.update({'_id': url}, {'$set': {'status': self.COMPLETE}})

    #
    def repair(self):
        """
         这个函数是重置状态$lt是比较 小于
         timestamp(属性) < 当前时间-超时时间(300)
        """
        record = self.db.find_and_modify(
            query={
                'timestamp': {'$lt': datetime.now() - timedelta(seconds=self.timeout)},
                'status': {'$ne': self.COMPLETE}
            },
            update={'$set': {'status': self.OUTSTANDING}}
        )
        if record:
            print('重置URL状态', record['_id'])

    def clear(self):
        """这个函数只有第一次才调用、后续不要调用、因为这是删库啊！"""
        self.db.drop()