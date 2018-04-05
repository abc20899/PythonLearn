# 导入模块  有一个文件名为june_class.py
# 则使用 import june_class
# persion = june_class.Persion('june',23)
# 每一个模块都有一个 _name_属性 当其值为 _main_ 时 表明模块自身运行
# from...import     from june_class import hello

"""导入模块"""
from src.basic.android.june_class import *

android = Android("7.1.1", "状态信息", "5", "nexus5", "32GB")
