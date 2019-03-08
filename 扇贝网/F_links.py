
# -*- coding:utf8 -*-

# 写个小脚本就搞定了！
import re

import pymysql

import time

import requests
from requests.exceptions import ConnectionError
from selenium import webdriver
from lxml import etree
import datetime











def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='SBW',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    for i in range(1,14689):
        sql = 'select link from Small_links where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        url = data['link']
        yield url

# 存储到MySQL中

def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='SBW',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany('insert into F_links (link) values (%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration:
        pass

# 转变为同时遍历两个列表，然后拼接的问题,还要制作一个数值的转变为字符串类型的列表
#  相当于两个不对等的容器，需要遍历，同时拼接字符串！
# 　两个不等长的列表，遍历优先于最短的哪个
# [""] 格式可以插入mysql
if __name__ == '__main__':
    for num in range(1, 11):
        for url_str in Python_sel_Mysql():
            url_f = url_str + "?page=" + str(num)
            into_url = []
            into_tuple = into_url.append((url_f))
            insertDB(into_url)
            print(datetime.datetime.now())










# 字段设置了唯一性 unique


# create table F_links(
# id int not null primary key auto_increment,
# link varchar(88)
# ) engine=InnoDB  charset=utf8;

# drop  table F_links;