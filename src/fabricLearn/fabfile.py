#coding=utf-8
# filename：fabfile.py
from fabric.context_managers import cd


def hello():
    print("Hello world!")

'''
$ fab hello
输出：hello world！
'''

# 带参数
def hello(name="world"):
    print("Hello %s!" % name)
'''
fab hello:name=Jeff
'''

#定义连接
# env.host确定要连接的远程服务器
# env.hosts = ['47.94.247.80']
# env.user = 'june'
# env.sudo_user = 'root'
def test():
    # do_test_stuff()
    pass

'''
fabric APIs
local(string of command)
在本地执行shell命令，命令以字符串的形式作为参数，如：
'''
from fabric.api import local
def prepare_deploy():
    local("git add -p && git commit")
    local("git push")

'''
run(string of command)
在远程服务器上'my_server'执行shell命令，命令以字符串的形式作为参数，如：
'''
from fabric.api import local
from fabric.operations import run
def deploy():
    code_dir = '/srv/django/myproject'
    with cd(code_dir):
        run("git pull")

'''
lcd(string of directory)
在本地执行目录切换操作，路径以字符串形式作为参数

cd(string of directory)
在远程服务器'my_server'上执行目录切换操作，路径以字符串形式作为参数

put(file, remote_directory)
把本地文件file上传到远程服务器的remote_directory目录下
'''


