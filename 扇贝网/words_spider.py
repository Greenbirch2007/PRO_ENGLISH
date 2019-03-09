
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

# driver = webdriver.Chrome()
from requests.exceptions import RequestException


# 请求

def get_first_page(url):
    # driver = webdriver.PhantomJS(service_args=SERVICE_ARGS)
    # driver.set_window_size(1200, 1200)  # 设置窗口大小
    # driver.get(url)
    # html = driver.page_source
    # time.sleep(6)
    # return html
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


# 把首页和翻页处理？
#　翻页有两个解决办法：
# 1. 倒叙遍历列表
# 2.点击下一页操作！
# 这个地方倾向于倒序遍历



# def next_page():
#     for i in range(1, 62):  # selenium 循环翻页成功！
#         driver.find_element_by_xpath('//*[@id="tbl_wrap"]/div/a[last()]').click()
#         time.sleep(3)
#         html = driver.page_source
#         return html


# 用遍历打开网页59次来处理

# print(html)  #正则还是有问题，选择了一个动态变动的颜色标记是不好的 最近浏览不是每次都有的！所以用数字的颜色取判断吧

def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！
    big_list = []
    selector = etree.HTML(html)
    words = selector.xpath('/html/body/div[3]/div/div[1]/div[2]/div/table/tbody/tr/td[1]/strong/text()')
    meanings = selector.xpath('/html/body/div[3]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/text()')
    s_contents = []
    for item in meanings:
        s = "".join(item.split("\n"))
        s_contents.append(s)

    for i1,i2 in zip(words,s_contents):
        big_list.append((i1,i2))
    return big_list





def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='SBW',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    for i in range(7900,146898):
        sql = 'select link from F_links where id = %s ' % i
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
        cursor.executemany('insert into words_contents (word,contents) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration:
        pass

if __name__ == '__main__':
    for url_str in Python_sel_Mysql():
        html = get_first_page(url_str)
        content = parse_html(html)
        insertDB(content)
        print(datetime.datetime.now())



# create table words_contents(
# id int not null primary key auto_increment,
# word varchar(50) ,
# contents text
# ) engine=InnoDB  charset=utf8;
#

# drop  table words_contents;