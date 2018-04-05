# coding=utf-8
import matplotlib.pyplot as plt  # 数学绘图库
import jieba  # 分词库

from wordcloud import WordCloud

# 1、读入文本数据
text = open('niuzaihenmang.txt', 'r').read()

# 2、结巴分词，默认精确模式。可以添加自定义词典userdict.txt,然后jieba.load_userdict(file_name),
# file_name为文件类对象或自定义词典的路径
# 自定义词典格式和默认词库dict.txt一样，一个词占一行：
# 每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒
cut_text = jieba.cut(text)
result = '/'.join(cut_text)  # 符号分隔开分词结果来形成字符串
# print(result)

# 3、生成词云图，这里需要注意的是WordCloud默认不支持中文，所以这里需已下载好的中文字库
# 无自定义背景图：需要指定生成词云图的像素大小，默认背景颜色为黑色,统一文字颜色：mode='RGBA'和colormap='pink'

wc = WordCloud(font_path='锐字工房云字库行楷GBK.ttf', background_color='white', width=800, height=800,
               max_font_size=50, max_words=1000)  # , min_font_size=10, mode='RGBA', colormap='pink')
wc.generate(result)
wc.to_file('wordcloud.png')

# 显示图片
plt.figure('yunci')  # 绘图名称
plt.imshow(wc)
plt.axis('off')  # 关闭坐标
plt.show()
