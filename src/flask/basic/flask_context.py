from flask import Flask, request, current_app, make_response, abort, redirect

app = Flask(__name__)

'''
1. flask 使用上下文临时把某些对象变为全局可访问，让特定的变量在一个线程中全局可访问，于此同时不会干扰其他线程

2. 上下文
程序上下文：current_app 当前激活程序的程序实例
           g      处理请求时用作临时存储的对象。每次请求都会重设这个变量
请求上下文：request 请求对象，封装了客户端发出的 HTTP 请求中的内容
           session 户会话，用于存储请求之间需要“记住”的值的词典

3. Flask 在分发请求之前激活(或推送)程序和请求上下文，请求处理完成后再将其删除。
   程序上下文被推送后，就可以在线程中使用 current_app 和 g 变量。类似地，
   请求上下文被 推送后，就可以使用 request 和 session 变量。如果使用这些变量时我们没有激活程序上下文或请求上下文，
   就会导致错误。

4. 请求调度
   Flask 会在程序的 URL 映射中查找请求的 URL。URL 映射是 URL 和视图函数之间的对应关系。 
   Flask 使用 app.route 修饰器或者非修饰器形式的 app.add_url_rule() 生成映射。   
    (venv) $ python
     >>> from hello import app
     >>> app.url_map
     Map([<Rule '/' (HEAD, OPTIONS, GET) -> index>,
      <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>, 
      <Rule '/user/<name>' (HEAD, OPTIONS, GET) -> user>])

5. 请求钩子
   before_first_request:注册一个函数，在处理第一个请求之前运行。
   before_request:注册一个函数，在每次请求之前运行。
   after_request:注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行。
   teardown_request:注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行。
   在请求钩子函数和视图函数之间共享数据一般使用上下文全局变量 g。例如，before_ request 
   处理程序可以从数据库中加载已登录用户，并将其保存到 g.user 中。随后调用视 图函数时，视图函数再使用 g.user 获取用户。

6. 响应 
   状态码200  302重定向  404 abort   

7. 扩展
   Flask 被设计为可扩展形式，故而没有提供一些重要的功能，例如数据库和用户认证，所
   以开发者可以自由选择最适合程序的包，或者按需求自行开发。         
   pip3 install flask-script
'''


# request 特定的对象
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return 'your browser is %s' % user_agent


@app.route('/bad')
def bad():
    return '<h3>Bad Request</h3>', 400


@app.route('/cookie')
def cookie():
    reponse = make_response('<h1>this is cookie')
    reponse.set_cookie('june', '31')
    return reponse


@app.route('/redirect')
def redi():
    return redirect('https://www.baidu.com')


@app.route('/user/<int:id>')
def user(id):
    if id < 0:
        abort(404)  # 交给web服务器处理
    return 'user id is %d' % id


if __name__ == '__main__':
    app_ctx = app.app_context()
    app_ctx.push()  # 必须push以后才能获取 current_app.name
    app_name = current_app.name
    print(app_name)  # flask_context  程序名称
    app_ctx.pop()
    app.run('127.0.0.1', 8080)
