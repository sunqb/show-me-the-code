#!/usr/bin/env python
# -*- coding: utf-8 -*-

'做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？'

__author__ = 'sunqb'

import sys
import random, string

reload(sys)
sys.setdefaultencoding('utf-8')

#生成num个len长度的code
def getCode(_length, _num):
    ALL_LETTERS = string.ascii_uppercase + string.digits
    result = []
    while(len(result) < _num):
        code = ''.join((random.choice(ALL_LETTERS) for i in range(_length)))
        result.append(code)
    for i in result:
        print i

if __name__ == '__main__':
    getCode(10, 200)