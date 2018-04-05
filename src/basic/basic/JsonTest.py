# json 库
"""
json与python数据类型的对应关系
{}  dict
[]  list
123.05  int或float
null  None
true/flase   True/False
"""

import json

#对数据进行编码
from enum import Enum

python_data = {'persions':[{'name':'june','age':29},{'name':'zhen','age':31}]} #一个字典
json_str = json.dumps(python_data) #转换成一个json
print(json_str)

json_data = '{"name":"june","age":29}'
python_dic = json.loads(json_data)
print(python_dic)

class VIP(Enum):
   YELLOW = 1
   GREEN = 2
   BLACK = 3
   RED = 4
print(VIP.YELLOW.value)