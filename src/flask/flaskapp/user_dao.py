from src.flask.flaskapp.user_model import *


@app.route('/user/v1.0/all', methods=['GET'])
def get_all():
    res = db.session.query(User).all()
    temp = []
    for x in res:
        temp.append(x.to_json())
    print(temp)
    return jsonify({'data': temp, 'code': 200})


@app.route('/user/v1.0/getuser', methods=['GET'])  # http://localhost/hello/user/v1.0/getuser?id=2
def getuser_by_id():
    # 在get请求下，request.form无法获取参数，其他两者都可以。
    getArgs = request.args
    res = User.query.filter(User.id == getArgs.get('id')).one()
    print(res.to_json())
    return jsonify({'data': res.to_json(), 'code': 200})


@app.route('/user/v1.0/adduser', methods=['POST'])
def add_user():
    print(request.values.get('username'))
    username = request.values.get('username')
    email = request.values.get('email')
    User(username, email).save()
    return 'ok'


@app.route('/user/v1.0/update', methods=['POST'])
def update_user():
    id = request.values.get('id')  # 更新哪个id的用户
    name = request.values.get('name')  # 更新的新名字
    user = User.query.filter(User.id == id).one()
    user.username = name
    user.save()  # 更新数据
    return 'ok'


@app.route('/user/v1.0/delete', methods=['POST'])
def delete_user():
    id = request.values.get('id')
    user = User.query.filter(User.id == id).one()
    if user is not None:
        db.session.delete(user)  # 删除用户
        db.session.commit()
    return 'ok'

# if __name__ == '__main__':
# u = User("hehe","abc20899@163.com")
# u.save()
