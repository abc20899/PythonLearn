"""
user model操作
综上，可以得出结论，
request.form.get("key", type=str, default=None) 获取表单数据，
request.args.get("key") 获取get请求参数，
request.values.get("key") 获取所有参数。
推荐使用request.values.get().
https://www.jianshu.com/p/7e32074e4fad
https://www.jianshu.com/p/4bb97fe23272
"""
from src.flask.flaskapp.flask_config import *

""" 
定义了三个字段， 数据库表名为model名小写
"""


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(120), unique=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

    def save(self):
        # db.drop_all()        #删除表
        db.create_all()  # 先创建表
        db.session.add(self)
        db.session.commit()

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
