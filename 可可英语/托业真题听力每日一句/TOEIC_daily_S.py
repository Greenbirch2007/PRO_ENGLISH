
# -*- coding:utf8 -*-

# 写个小脚本就搞定了！
import re

import pymysql

import time
from requests.exceptions import ConnectionError
from selenium import webdriver
from lxml import etree
import datetime

driver = webdriver.Chrome()


# 请求

def get_first_page(url):
    # driver = webdriver.PhantomJS(service_args=SERVICE_ARGS)
    driver.set_window_size(1200, 1200)  # 设置窗口大小
    driver.get(url)
    html = driver.page_source
    time.sleep(6)
    return html


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

# def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！
#     big_list = []
#     selector = etree.HTML(html)
#     title = selector.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/ul//h2/a[2]/text()')
#     mp3_link = selector.xpath('//*[@id="tbl_wrap"]/table/tbody/tr/th[2]/a/text()')
#     for i1, i2 in zip(title, mp3_link):  # 两个列表分别遍历然后组成一个新的元组，或新的列表！
#         title_f = i1[11:]
#         link_f = "http://www.kekenet.com/mp3" + i2[6:]
#         big_list.append((title_f,link_f))


# lxml解析失效，只能使用正则

def parse_html(html):
    patt = re.compile('<a href="(.*?)" title="(.*?)" target="_blank",re.S>')
    items = re.findall(patt,html)
    pass





'http://www.kekenet.com/toeic/201806/549088.shtml' # 最终map３
'http://www.kekenet.com/toeic/201806/549088.shtml'
'http://www.kekenet.com/mp3/201806/549088.shtml'

'/toeic/201806/549088.shtml'


# 存储到MySQL中

def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='hk_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany('insert into hk_stock (code,name) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration:
        pass


# if __name__ == '__main__':
#     html = get_first_page()
#     content = parse_html(html)
#     time.sleep(3)
#     insertDB(content)
#     while True:
#         html = next_page()
#         content = parse_html(html)
#         insertDB(content)
#         print(datetime.datetime.now())
#

url = 'http://www.kekenet.com/toeic/'
html = get_first_page(url)
parse_html(html)

# 字段设置了唯一性 unique

# create table hk_stock(
# id int not null primary key auto_increment,
# code varchar(12) unique,
# name varchar(50)
# ) engine=InnoDB  charset=utf8;

# 传入url太快了，考虑分成两部分完成：1.先存到数据库中或其他容器中（数据结构不行）
#  2. 再从数据库中逐个调取进行爬取   3. 中间过渡的数据库是用内存型（redis) 还是一般存储型的？
# 4.数据量小，爬取，传入，再解析影响不大，但是分布式爬取大量数据，就必须要切割开来，才能各司其职，有效处理各自的工作！
# 5.容器是必备，分布式必备，代理池也是必备

