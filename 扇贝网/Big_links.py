
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

from requests.exceptions import RequestException

# 请求

def get_first_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None



def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！
    big_list = []
    selector = etree.HTML(html)
    links = selector.xpath('//div[@title]/a/@href')
    for item in links:
        complete_link = "https://www.shanbay.com" + item
        big_list.append(complete_link)
    return big_list









# 存储到MySQL中

def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='SBW',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany('insert into Big_links (link) values (%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration:
        pass


if __name__ == '__main__':
    url = 'https://www.shanbay.com/wordbook/category/150/'
    html = get_first_page(url)
    content = parse_html(html)
    time.sleep(3)
    insertDB(content)



# 字段设置了唯一性 unique

# create table Big_links(
# id int not null primary key auto_increment,
# link varchar(88)
# ) engine=InnoDB  charset=utf8;

