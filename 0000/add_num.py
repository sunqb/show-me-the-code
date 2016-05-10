#!/usr/bin/env python
# -*- coding: utf-8 -*-

' 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果'

__author__ = 'sunqb'

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#PIL这个包win下面需要去官网下载，其他平台请百度
from PIL import Image, ImageDraw, ImageFont, ImageFilter

#加数字
def add_num(picPath, num):
    img = Image.open(picPath)
    x, y = img.size
    myfont = ImageFont.truetype('D:/Futura.ttf', x / 3)
    ImageDraw.Draw(img).text((2 * x / 3, 0), str(num), font = myfont, fill = 'red')
    img.save('D:/pic_with_num.jpg')

#模糊图片，还有其他搜索Image.filter
def filterImg(picPath):
    img = Image.open(picPath)
    img2 = img.filter(ImageFilter.BLUR)
    img2.save('D:/pic_filter_img.jpg')

#图片缩放
def img_mx(picPath):
    img = Image.open(picPath)
    x, y = img.size
    img.thumbnail((x/2, y/2))
    img.save('D:/pic_img_mx.jpg', 'jpeg')

if __name__ == '__main__':
    # add_num('D:/pic.jpg', 9)
    #filterImg('D:/pic.jpg')
    #img_mx('D:/pic.jpg')