#!/usr/bin/python
# coding=utf-8
# 'latin-1' codec can't encode characters in position 40-41: ordinal not in range(256)
# 解决 数据库连接时charset="utf8"
import json
import logging

import os
import pymysql

# 建立连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     db='learnPython',
                     charset="utf8")

class meizi_bean(object):
    title = ''
    urls = []

    def __init__(self, title, urls):
        self.title = title
        self.urls = urls

    def to_json(self):
        return {
            'title': self.title,
            'urls': self.urls
        }

    def create_table(self):
        # 创建表 persion
        sql = '''
          create table if not exists meizi(
          id int NOT NULL AUTO_INCREMENT,
          title text,
          urls text,
          PRIMARY KEY (`id`)
          )
          '''
        # 使用cursor() 创建一个游标对象
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            db.commit()  # 提交事务
            print('create table success')
        except BaseException as e:  # 如果发生错误回滚
            db.rollback()
            print(e)
        finally:
            cursor.close()  # 关闭游标
            db.close()  # 关闭数据库

    #修改数据表
    def modify_table(self,sql):
        # sql = 'ALTER TABLE table_name ADD field_name field_type'
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            db.commit()  # 提交事务
            print('modify table success')
        except BaseException as e:  # 如果发生错误回滚
            db.rollback()
            print(e)
        finally:
            cursor.close()  # 关闭游标
            db.close()  # 关闭数据库

    #插入数据
    def insert_meizi(self, title, urls):
        sql = 'insert into meizi (title,urls) values (%s,%s)'
        sqlquery = 'select * from meizi where title = %s'
        cursor = db.cursor()
        try:
            #查询是否已经插入数据
            cursor.execute(sqlquery,title)
            result = cursor.fetchone()
            if result == None:
                value = (title, urls)
                cursor.execute(sql, value)  # 插入数据
                db.commit()
                print('insert table success')
        except BaseException as e:
            db.rollback()
            print(e)
        finally:
            cursor.close()
            db.close()

    def update_meizi(self,title,category):
        sql = 'update meizi set category=%s where title=%s'
        cursor = db.cursor()
        try:
            # 更新数据
            value = (category,title)
            cursor.execute(sql, value)  # 插入数据
            db.commit()
            print('update table success')
        except BaseException as e:
            db.rollback()
            print(e)
        finally:
            pass
            # cursor.close()
            # db.close()

    def update_urls(self,title,urls):
        sql = 'update meizi set urls=%s where title=%s'
        cursor = db.cursor()
        try:
            # 更新数据
            value = (urls, title)
            cursor.execute(sql, value)  # 插入数据
            db.commit()
            print('update table success')
        except BaseException as e:
            db.rollback()
            print(e)
        finally:
            pass
            # cursor.close()
            # db.close()

    #查询是否存在
    def query_meizi(self, title):
        sqlquery = 'select * from meizi where title = %s'
        cursor = db.cursor()
        try:
            # 查询是否已经插入数据
            cursor.execute(sqlquery, title)
            result = cursor.fetchone()
            if result == None:
               print('数据库不存在此条记录')
               return True
            else:
               print('此条记录存在')
               return False
        except BaseException as e:
            db.rollback()
            print(e)
        finally:
            pass
            # cursor.close()
            # db.close()

    # count:100045
    def list_file(self,rootDir):
        global count
        global urls
        for lists in os.listdir(rootDir):
            path = os.path.join(rootDir, lists)
            if os.path.isfile(path) and '.DS_Store' not in path:
               count+=1
               print('count:'+str(count))
               title = os.path.abspath(path).split('/')[-2]
               imgdic = {'url':path.split('/')[-1]}
               urls.append(imgdic)
               print(title,urls)
               if self.query_meizi(title):
                   logging.info(title)
               else:
                   self.update_urls(title, json.dumps(urls))  # 更新数据
            if os.path.isdir(path):
                urls.clear()
                self.list_file(path)

if __name__ == '__main__':
    urls = []
    count = 0
    meizi = meizi_bean('',[])
    path = '/Users/junzhao/python/meiziimg'
    logging.basicConfig(filename='meizi.log', level=logging.INFO)
    meizi.list_file(path)
#     print(json.dumps(urls))
#     meizi.create_table()
#     # meizi.insert_meizi('测试2', json.dumps(urls))
#     print(meizi.query_meizi('测试222'))
#     sql = 'ALTER TABLE meizi ADD category text'
#     meizi.update_meizi('松果儿热辣勾魂真空上阵 透视蕾丝大胆展示傲人曲线','性感妹子')