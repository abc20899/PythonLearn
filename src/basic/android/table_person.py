"""
操作persion表
pip3 install flask-sqlalchemy pymysql

使用Flask-SQLAlchemy管理数据库
Flask-SQLAlchemy是一个Flask扩展，它简化了在Flask应用程序中对SQLAlchemy的使用。
SQLAlchemy是一个强大的关系数据库框架，支持一些数据库后端。提供高级的ORM和底层访问数据库的本地SQL功能。
http://docs.sqlalchemy.org/en/latest/dialects/mysql.html
"""
import pymysql
import json

#返回sql连接
def person_db():
    return pymysql.connect(
                         host='localhost',
                         user='root',
                         password='123456',
                         db='learnPython',
                         charset="utf8")  #插入中文
results = None
def query_all():
    sql = 'select * from person'
    db = person_db()
    cursor = db.cursor()
    global results
    try:
        cursor.execute(sql)
        #cursor.scroll(0, mode='absolute')
        results = cursor.fetchall() #返回一个元组对象
        print(json.dumps(results)) #[[2, "jie", 18, "coder", 0], [3, "haha", 28, "doctor", 0]]
    except BaseException as e:
        db.rollback()
        print(e)
    finally:
        cursor.close()
        db.close()
    return results

def query_by_id(id):
    sql = 'select * from person where id = %s'
    db = person_db()
    cursor = db.cursor()
    try:
        cursor.execute(sql,id)
        result = cursor.fetchone()
        print(result)
    except BaseException as e:
        db.rollback()
        print(e)
    finally:
        cursor.close()
        db.close()
    return result

#插入一个person对象
success = False
def insert_person(person):
    sql = 'insert into persion (name,age,job,sex) values (%s,%s,%s,%s)'
    db = person_db()
    cursor = db.cursor()
    global success
    try:
        value = (person.name,person.age,person.job,person.sex)
        success = cursor.execute(sql,value)
        db.commit()
    except BaseException as e:
        db.rollback()
        print(e)
    finally:
        cursor.close()
        db.close()
    return success

def update_person(person):
    sql = 'update persion set name=%s,age=%s,job=%s,sex=%s where id=%s'
    db = person_db()
    cursor = db.cursor()
    try:
        vaule = (person.name,person.age,person.job,person.sex,person.id)
        success = cursor.execute(sql,vaule)
        db.commit()
    except BaseException as e:
        db.rollback()
        print(e)
    finally:
        cursor.close()
        db.close()
    return success

#删除数据
def delete_person(id):
    sql = 'delete from persion where id=%s'
    db = person_db()
    cursor = db.cursor()
    try:
        success = cursor.execute(sql,id)
        db.commit()
    except BaseException as e:
        db.rollback()
        print(e)
    finally:
        cursor.close()
        db.close()
    return success

#if __name__ == '__main__':
#    delete_person(4)