'''
mysql.server start
mysql -u root -p
sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED BY '123456'; 修改root密码
'''
import pymysql

#创建表
def create_table():
    #建立连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='123456',
                         db='learnPython')
    #创建表 persion
    sql = '''
    create table if not exists persion(
    id int NOT NULL AUTO_INCREMENT,
    name text,
    age int,
    job text,
    sex int,
    PRIMARY KEY (`id`)
    )
    '''
    #使用cursor() 创建一个游标对象
    cursor = db.cursor()
    try:
        #执行sql语句
        cursor.execute(sql)
        db.commit() #提交事务
        print('create table success')
    except BaseException as e: #如果发生错误回滚
        db.rollback()
        print(e)
    finally:
        cursor.close() #关闭游标
        db.close() #关闭数据库

#create_table() #调用创建数据表

def insert_table():
    # 建立连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='123456',
                         db='learnPython')
    sql = 'insert into persion (name,age,job,sex) values (%s,%s,%s,%s)'
    cursor = db.cursor()
    try:
        value = ("zhaojie",28,"worker",0)
        cursor.execute(sql,value) #插入数据
        db.commit()
        print('insert table success')
    except BaseException as e:
        db.rollback()
        print(e)
    finally:
        cursor.close()
        db.close()
#insert_table() #调用插入数据库


def query_table():
    # 建立连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='123456',
                         db='learnPython')
    sql = 'select * from persion'
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        #查询一条记录
        result_1 = cursor.fetchone()
        print(result_1)
        #如果先用fetchone 游标从1开始
        #relative 从当前所在的行开始移动，absolute从第一行开始移动
        cursor.scroll(0,mode='absolute')
        #查询多条记录
        results = cursor.fetchall()
        for row in results:
            print(row)
    except BaseException as e:
        db.rollback()
        print(e)
    finally:
        cursor.close()
        db.cursor()
#query_table() #调用查询

def update_table():
    # 建立连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='123456',
                         db='learnPython')
    #更新语句
    sql = 'update persion set name=%s where id=%s'
    cursor = db.cursor()
    try:
        value = ('jie',2)  #更新第二个数据
        cursor.execute(sql,value)
        db.commit()
        print('update success')
    except BaseException as e:
        db.rollback()
        print(e)
    finally:
        cursor.close()
        db.close()
#update_table() #调用更新

def delete_table():
    # 建立连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='123456',
                         db='learnPython')
    #删除id = 1
    sql = 'delete from persion where id=%s'
    cursor = db.cursor()
    try:
        cursor.execute(sql,1)
        db.commit()
        print('delete success')
    except BaseException as e:
        db.rollback()
        print(e)
    finally:
        cursor.close()
        db.close()
if __name__ == '__main__':
 insert_table() #调用删除