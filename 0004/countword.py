#!/usr/bin/env python
# -*- coding: utf-8 -*-

'第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数'

__author__ = 'sunqb'

import sys
from collections import Counter
import re

reload(sys)
sys.setdefaultencoding('utf-8')

#读取文件，一行一行处理
def readFile(filename):
    datalist = []
    with open(filename, 'r') as f:
        for line in f:
            #特殊字符处理
            content = re.sub("\"|,|\.", "", line)
            datalist.extend(content.strip().split(' '))
    return datalist

#调用计数器
def wc(filename):
    print Counter(readFile(filename))


if __name__ == '__main__':
    wc('''aomanyupianjian''')