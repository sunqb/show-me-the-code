#!/usr/bin/env python
# -*- coding: utf-8 -*-

'第 0004 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小'

__author__ = 'sunqb'

import sys
import os
from PIL import Image

IPHONE5_WIDTH = 1136
IPHONE5_HEIGHT = 640

reload(sys)
sys.setdefaultencoding('utf-8')

# 改变一张图片的分辨率
def reset_pic_size(file_path, new_path, width = IPHONE5_WIDTH, height = IPHONE5_HEIGHT):
    image = Image.open(file_path)
    image_width, image_height = image.size
    if image_width > width:
        image_height = width * image_height // image_width
        image_width = width
    if image_height > height:
        image_width = height * image_width // image_height
        image_height = height

    new_image = image.resize((image_width, image_height), Image.ANTIALIAS)
    new_image.save(new_path)

# 从文件夹中循环改变每一张图片
def find_and_resize_pic_from_dir(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file_name in files:
            if file_name.lower().endswith('jpg') or file_name.lower().endswith('png'):
                file_path = os.path.join(root, file_name)
                file_new_path = 'iPhone5_' + file_name
                reset_pic_size(file_path, file_new_path)

if __name__ == '__main__':
    find_and_resize_pic_from_dir('''D:/images''')