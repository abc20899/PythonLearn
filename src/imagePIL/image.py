# coding=utf-8
#matplotlib是一个专业绘图的库
# pip3 install Pillow
# http://pillow-cn.readthedocs.io/zh_CN/latest/
#pip3 install matplotlib
import os

from PIL import Image, ImageFilter
import numpy as np
import matplotlib.image as mpimg

mask_path = '/Users/junzhao/python/qianlongmask.png'

def read_pic(path):
    im = Image.open(path)
    im.show()  #显示图片

#创建缩略图
def thumb_pic(path_src,path_des=None):
    filename_ext = path_src.split('/')[-1] #文件名字带后缀 23c06.jpg
    filename = filename_ext.split('.')[0] #文件名字23c06
    fileparent_arr = path_src.split('/')[0:-1] #['', 'Users', 'junzhao', 'python', 'meiziimg', '高挑美女若彤']
    fileparent = ''
    for dir in fileparent_arr:
        fileparent += dir+'/'    #/Users/junzhao/python/meiziimg/高挑美女若彤/
    img = Image.open(path_src)
    size = img.size       # (700, 1050)
    format = img.format   # JPEG
    mode = img.mode       # RGB
    thumb = (size[0]*0.3, size[1]*0.3) #缩放0.3倍
    img.thumbnail(thumb)   #创建缩略图
    if path_des is not None:
        img.save(path_des, format)  # 按原始格式保存
    else:
        filename = filename+'_thumbnail.'+format
        img.save(fileparent+filename, format)  # 按原始格式保存
    print('thumb success')

#旋转图片
def rorate(path_src,style=None):
    img = Image.open(path_src)
    if style is None:
        style = Image.FLIP_LEFT_RIGHT #左右旋转
    rorate = img.transpose(style) #旋转方式 Image.FLIP_LEFT_RIGHT
    rorate.show()

#缩放图片 百分比
def scale(path_src,percent=None):
    img = Image.open(path_src)
    size = img.size
    if percent is None:
        percent = 0.3
    resize = (int(size[0]*percent),int(size[1]*percent))
    resize_img = img.resize(resize)
    resize_img.show()

#色彩变化 色彩空间的转换
'''
1 1位像素，黑和白，存成8位的像素
L 8位像素，黑白
P 8位像素，使用调色板映射到任何其他模式
RGB 3×8位像素，真彩
RGBA 4×8位像素，真彩+透明通道
CMYK 4×8位像素，颜色隔离
YCbCr 3×8位像素，彩色视频格式
I 32位整型像素
F 32位整型像素
'''
def convert(pic_path):
    img = Image.open(pic_path)
    new_img = img.convert('CMYK')
    new_img.show()

#像素点改变
def putpixel(pic_path):
    img = Image.open(pic_path)
    print(img.getpixel((100,100))) #打印(100,100)处的像素值
    img.putpixel((100,100),(0,0,0)) #改变(100,100)处的像素值

#剪裁
def crop(pic_path):
    img = Image.open(pic_path)
    size = img.size
    box = (0,0,size[0],int(size[1]*0.97))  #剪裁区域
    new_img = img.crop(box)
    new_img.show()

#point像素点处理
def point(pic_path):
    img = Image.open(pic_path)
    source = img.split()
    R, G, B = 0, 1, 2
    mask = source[R].point(lambda i: i < 100 and 255)
    out = source[G].point(lambda i: i * 0.7)
    source[G].paste(out, None, mask)
    # new_img = Image.merge(img.mode, source)
    # new_img.show()

    print(img.getpixel((100,100)))  #(244, 239, 236) 打印100,100处的像素值
    arr = np.array(img)   #将PIL对象转换为数组对象  img[i,j,k]
    # for point in arr:
    #    print(point)

    # new_img = Image.fromarray(arr)  #将数组转换为图像
    # new_img.show()

    #直接对图像像素点进行修改
    #将每个像素点的亮度增大20%
    # out = img.point(lambda i: i * 1.2 + 10)  # lambda匿名函数 返回输入i 返回 i*1.2+10
    # out.show()

    size = img.size
    box = (0, int(size[1] * 0.97), size[0],size[1])  # 最底部区域
    new_img = img.crop(box)
    new_img.convert('RGBA')
    pix = new_img.load()
    width = new_img.size[0]
    height = new_img.size[1]
    for x in range(width):
        for y in range(height):
            r, g, b = pix[x, y]
            print(r,g,b)   #打印所有像素点
            if r > 120 and g > 120 and b > 120:
                r = 0
                g = 0
                b = 0
                a = 255
            pix[x, y] = r,g,b,a
    new_img.show()

def filter(pic_path):
    img = Image.open(pic_path)
    size = img.size
    box = (0, int(size[1] * 0.97), size[0], size[1])  # 最底部区域
    crop_img = img.crop(box).filter(ImageFilter.BLUR) #剪切的部分进行滤镜 BLUR
    # crop_img.show()
    #处理子图，粘贴回原图
    img.paste(crop_img, box)
    img.show()

def alpha_img(pic_path):
    img = Image.open(pic_path)
    size = img.size
    box = (0, int(size[1] * 0.96), size[0], size[1])  # 最底部区域
    crop_img = img.crop(box) #剪切
    crop_img = crop_img.convert('RGBA') #转换成四通道
    pixs = crop_img.load()  #取得像素数组
    width,height = crop_img.size
    for x in range(width):
        for y in range(height):
            r, g, b,a = pixs[x, y]
            print(r, g, b, a)  # 打印所有像素点
            if r >= 122 and g >= 122 and b >= 122:
                r = 0
                g = 0
                b = 0
                a = 255
                pixs[x, y] = r, g, b, a
    #处理子图，粘贴回原图
    img.paste(crop_img, box)
    img.show()

def add_mask(pic_path):
    img = Image.open(pic_path)
    mark = Image.open(mask_path)
    layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
    layer.paste(mark, (img.size[0] - 150, img.size[1] - 40))  #粘贴
    out = Image.composite(layer, img, layer)
    out.show()

def process_img(pic_path):
    try:
        img = Image.open(pic_path)
        box = (0, 0, img.size[0], int(img.size[1] * 0.961))  # 剪裁区域
        crop_img = img.crop(box)
        mark = Image.open(mask_path)
        mark_layer = Image.new('RGBA', crop_img.size, (0, 0, 0, 0))  #创建一张和crop_img大小一样的图片
        mark_layer.paste(mark, (crop_img.size[0] - 150, crop_img.size[1] - 40))  # 粘贴mask上去
        out = Image.composite(mark_layer, crop_img, mark_layer)
        out.save(pic_path,img.format,quality=100)
    except BaseException as e:
        write_exception(pic_path+"  "+str(e))  #将异常路径写入文件
        print(e)
        pass

count = 0   #100179张
def list_file(rootDir):
    global count
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        if os.path.isfile(path) and '.DS_Store' not in path:
           count+=1
           print('开始处理图片第'+str(count)+"张")
           process_img(path)    #处理图片
           print(path+str("处理完成"))
        if os.path.isdir(path):
            list_file(path)

def write_exception(message):
    f = open('./error.txt', 'a')  # 写模式 在当前目录下创建一个文件 a 可追加
    f.write(message+'\n')

if __name__ == '__main__':
    base_path = '/Users/junzhao/python/meiziimg/'
    # filename = '05a03.jpg'
    # pic_path = base_path + filename
    # process_img(pic_path)
    list_file(base_path)