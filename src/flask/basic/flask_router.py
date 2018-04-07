from flask import Flask

# 实例化Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"


# 动态url  动态部分默认为string类型
# 动态类型为 <int:id>、<float:price>、<path:url> path /不作为分割部分
@app.route("/user/<name>")
def user(name):
    return '<h1>Hello,%s!</h1>' % name

#http://127.0.0.1:8080/book/12.344
@app.route("/book/<float:price>")
def book(price):
    return '<h3>book is %f</h3>' % price


if __name__ == '__main__':
    # app.run(debug=True)
    app.run('127.0.0.1', 8080)
