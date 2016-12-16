#!/usr/bin/env python
# -*- coding: utf-8 -*-

'将 0001 题生成的 200 个激活码（或者优惠券）保存到 redis数据库中。'

__author__ = 'sunqb'

import sys
import random, string
import redis
import time

reload(sys)
sys.setdefaultencoding('utf-8')

#redis连接
conn = redis.Redis(host='localhost', port=6379, db=0)
pipeline = conn.pipeline()

#生成num个len长度的code
def getCode(_length, _num):
    ALL_LETTERS = string.ascii_uppercase + string.digits
    result = []
    while(len(result) < _num):
        code = ''.join((random.choice(ALL_LETTERS)  for i in range(_length)))
        result.append(code)
    for i in result:
        print i
    return result

#保存到数据库
def save2db(codelist):
    for code in codelist:
        pipeline.lpush('randomCodeRedis', code)
        pipeline.execute()

if __name__ == '__main__':
    save2db(getCode(10, 200))