#捕获异常

try:
    name = '128s'
    print(int(name))
except ValueError as e: #异常基类BaseException
    print(e)
finally:
    print('finally')