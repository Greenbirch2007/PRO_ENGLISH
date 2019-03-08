
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

driver = webdriver.Chrome()



# 请求

def get_first_page(url):
    driver.set_window_size(1200, 1200)  # 设置窗口大小
    driver.get(url)
    html = driver.page_source
    time.sleep(6)
    return html


def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！
    big_list = []
    selector = etree.HTML(html)
    links = selector.xpath('//*[@id="wordlist-"]/div[1]/table/tbody/tr/td[1]/a/@href')
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
        cursor.executemany('insert into Small_links (link) values (%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration:
        pass


def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='SBW',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    for i in range(1,1403):
        sql = 'select link from Big_links where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        url = data['link']
        yield url



if __name__ == '__main__':
    for url_str in Python_sel_Mysql():
        html = get_first_page(url_str)
        content = parse_html(html)
        insertDB(content)
        print(datetime.datetime.now())




# 字段设置了唯一性 unique


# create table Small_links(
# id int not null primary key auto_increment,
# link varchar(88)
# ) engine=InnoDB  charset=utf8;

