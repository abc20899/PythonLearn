"""
pip3 install flask
测试

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 243-606-415

 nginx用于转发各种服务
 brew install nginx  #/usr/local/Cellar/nginx/1.12.2_1
 nginx  #启动默认 8080端口
 nginx -s reload|reopen|stop|quit  #重新加载配置|重启|停止|退出 nginx
 /usr/local/etc/nginx/nginx.conf     配置文件路径
 /usr/local/var/www     服务器默认路径
 /usr/local/Cellar/nginx/1.12.2_1/bin/nginx  启动nginx的路径

http://python.jobbole.com/84286/ 参考
https://www.jianshu.com/p/9c880ee8eab8 参考
 Nginx是一个提供静态文件访问的web服务，然而，它不能直接执行托管Python应用程序，而uWSGI解决了这个问题。让我们先安装uWSGI，
 sudo pip install uwsgi   //部署py应用
 pip3 install virtualenv   //用于创建虚拟环境
我们将托管的应用是经典的“Hello, world!”。这个应用只有一个页面
将所有应用相关的文件存放在/var/www/demoapp文件夹中
sudo chown -R ubuntu:ubuntu /var/www/demoapp/
cd /var/www/demoapp
virtualenv hellworld  //创建虚拟环境
. venv/bin/activate   //进入虚拟环境
pip3 install flask    //安装flask

创建hello.py文件
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
执行 python3
现在应用是由Flask内置的web服务托管的，对于开发和调试这确实是个不错的工具，但不推荐在生产环境中使用
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello flaskapp'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) # flasktest 自带服务器


