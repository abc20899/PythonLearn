'''
http://www.runoob.com/mongodb/mongodb-osx-install.html
sudo brew install mongodb
sudo brew install mongodb --devel #安装最新开发版本：

安装目录为:
sudo /usr/local/Cellar/mongodb/3.6.2/bin/mongod

运行 MongoDB:
sudo mkdir -p /data/db
启动 mongodb，默认数据库目录即为 /data/db：
sudo mongod
# 如果没有创建全局路径 PATH，需要进入以下目录
cd /usr/local/mongodb/bin
sudo ./mongod

demo:
$ cd /usr/local/mongodb/bin
$ ./mongo
MongoDB shell version v3.4.2
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.4.2
Welcome to the MongoDB shell.
……
> 1 + 1
2
>


python3 操作
pip3 install pymongo
'''
import json

from pymongo import MongoClient

class Mogo():
   def __init__(self):
       conn = MongoClient('mongodb://localhost:27017/')
       self.db = conn.persiondb  # 连接数据库名

   def insert(self):
       for i in range(5,100):
        self.db.col.insert({'name':'june'+str(i),'age':22,'sex':1})

   '''
      db.col.find().sort("id")  #默认为升序
      db.col.find().sort("id",pymongo.ASCENDING)   #升序
      db.col.find().sort("id",pymongo.DESCENDING)  #降序
      db.col.find({"by":"菜鸟教程"}).pretty()	where by = '菜鸟教程'
      db.col.find({"likes":{$lt:50}}).pretty()	where likes < 50
      db.col.find({"likes":{$lte:50}}).pretty()	where likes <= 50
      db.col.find({"likes":{$gt:50}}).pretty()	where likes > 50
      db.col.find({"likes":{$gte:50}}).pretty()	where likes >= 50
      db.col.find({"likes":{$ne:50}}).pretty()	where likes != 50
      '''
   def query(self):
       for item in self.db.col.find():
           print(item)
       pass

   def querybyname(self,keyword):
       item = self.db.col.find_one({"name": keyword})
       print(item)

   '''
   db.col.update(
   <query>,
   <update>
   db.col.update({'title':'MongoDB 教程'},{$set:{'title':'MongoDB'}},{multi:true})
   multi 修改多条记录
   '''
   def update(self,query,update):
       try:
           self.db.col.update(query, {'$set': update})
       except BaseException as e:
           print(e)

   '''
   db.col.remove()  全部删除
   db.col.remove({"user_name":"xiao"}) 删除指定记录
   justOne : （可选）如果设为 true 或 1，则只删除一个文档。
   '''
   def delete(self,query):
      self.db.col.remove(query)

if __name__ == '__main__':
    # Mogo().insert()
    # Mogo().querybyname('june33')
    # Mogo().update({'name':'june22'},{'age':222})
    # Mogo().querybyname('june22')
    # Mogo().delete({'name':'june33'})
    Mogo().querybyname('june33')