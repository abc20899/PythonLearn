# -*- coding: utf-8 -*-
import sys
import os
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'jobbole'])
# print(os.path.dirname(os.path.abspath(__file__)))

# scrapy shell url 调试

# xpath
# 父节点 子节点 同胞节点 先辈节点 后辈节点
# article 选取所有article元素的所有子节点
# /article 选取根元素article
# article/a 选取所有属于article的子元素的a元素
# //div    选取所有div子元素(不论出现在文档的任何地方)
# article//div  选取所有article元素的后代的div元素，不管在article之下的任何位置
# //@class  选取所有名为class 的元素
# /article/div[1] article下的第一个div
# /article/div[last()]  article下的最后一个div
# /article/div[last()-1]  article下的倒数第二个div
# //div[@lang]  拥有lang属性的所有div
# //div[@lang='eng']  属性lang为eng的所有div
# /div/*  选取属于div元素的所有子节点
# //*  选取所有元素
# //div[@*] 选取所有带属性的title元素
# /div/a|//div/p 选取所有div元素的a和p的元素
# //span|//ul 选取文档中的span和ul元素
# article/div/p|//span 所有属于article元素的div元素的p元素  以及文档中的所有span元素


# css选择器
# * 选取所有节点
# #container 选取id为container的节点
# .container  选取所有class为container的节点
# li a 选取所有li下的所有a节点
# ul+p 选取ul后面的第一个p元素
# div#container > ul  选取id为container的div标签第一个ul节点
# ul~p 选取与ul相邻的所有p元素
# a[title] 选取所有有title属性的a元素
# a[href='']
