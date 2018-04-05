"""
user 服务器与数据库连接配置
"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from src.flask.flaskapp.database_config import DB_URI

'''配置数据库'''
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
# 设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 初始化
db = SQLAlchemy(app)
