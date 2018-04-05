from datetime import datetime

from src.flask.flaskapp.flask_config import *

"""
用户同成绩单之前是一对多的关系
"id"：整型主键
"course"：最大长度为 50 的字符串
"assess_date"：日期时间类型
"score"：浮点型
"is_pass"：布尔型

user = db.relationship('User',backref=db.backref('scroes',lazy='dynamic'))
使得我们可以通过"Score.user"访问当前 score 记录的 user 对象，它的第一个参数"User"就表明了对应的对象模型是 User。
而第二个参数"backref"定义了从 User 模型反向引用 Score 模型的方法，上例中，我们就可以用"User.scores"获取当前 user 
对象所有的 score 记录，它是一个列表。"db.backref()"方法的"lazy"参数决定了在 User 
对象中什么时候加载其 scores 列表的值，延迟加载可以提高性能，并避免内存的浪费，
"""


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course = db.Column(db.String(50))
    assess_date = db.Column(db.DateTime)
    score = db.Column(db.Float)
    is_pass = db.Column(db.Boolean)

    # "user_id"：整型外键，对应于"user"表的主键"id"
    # "user_id"字段声明了外键，也就相当于声明了"user"表同"score"表的一对多关系
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # user 通过scroes查询所有课程
    user = db.relationship('User', backref=db.backref('scroes', lazy='dynamic'))

    def __init__(self, course, score, user, assess_date=None):
        self.course = course
        self.score = score
        self.is_pass = (score >= 60)
        if assess_date is None:
            assess_date = datetime.now()
        self.assess_date = assess_date
        self.user = user

    def __repr__(self):
        return '<Course %r of User %r>' % (self.course, self.user.name)

    def to_json(self):
        return {
            'id': self.id,
            'course': self.course,
            'assess_date': self.assess_date,
            'score': self.score,
            'is_pass': self.is_pass
        }
