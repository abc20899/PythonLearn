from flask import app, request, jsonify

from src.flask.flaskapp.flask_config import db
from src.flask.flaskapp.score_model import *
from src.flask.flaskapp.user_model import User


# 添加分数 为用户
@app.route('/user/v1.0/addscore', methods=['POST'])
def add_score():
    userid = request.values.get('id')  # 用户id
    course = request.values.get('course')  # 科目
    score = float(request.values.get('score'))  # 分数 转换为 float
    user = User.query.filter(User.id == userid).one()
    if user is not None:
        db.create_all()
        db.session.add(Score(course, score, user))
        db.session.commit()
    return 'ok'


# 获取所有分数
@app.route('/user/v1.0/getscore', methods=['GET'])
def get_scores():
    userid = request.args.get('id')
    user = User.query.filter(User.id == userid).one()
    if user is not None:
        score_arr = []
        for score in user.scroes:
            score_arr.append(score.to_json())
        # user.scroes = score_arr
    return jsonify({'data': score_arr, 'code': 200})


@app.route('/')
def hello():
    return 'hello world'


@app.route('/hello2')
def hello2():
    return 'hello2 app'
