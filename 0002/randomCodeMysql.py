#!/usr/bin/env python
# -*- coding: utf-8 -*-

'将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。'

__author__ = 'sunqb'

import sys
import random, string
import mysql.connector
import time

reload(sys)
sys.setdefaultencoding('utf-8')

#mysql数据库连接
conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='root', database='pmysql', use_unicode=True)
cursor = conn.cursor()

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
    try:
        for code in codelist:
            vsql = '''insert into t_code(code,time) values (%s,%s)'''
            #vsql = vsql.encode('utf8')
            cursor.execute(vsql, [code, getTime()])
        conn.commit()
        cursor.close()
        conn.close()
    except:
        conn.rollback()

#获取当前时间
def getTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

if __name__ == '__main__':
    save2db(getCode(10, 200))