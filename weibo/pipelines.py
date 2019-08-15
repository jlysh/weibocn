# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class WeiboPipeline(object):
    def __init__(self):
        #创建连接
        self.conn = pymysql.connect('localhost','root','root','sina')
        #创建游标
        self.cursor = self.conn.cursor()
    #管道处理，将数据存入mysql
    def process_item(self, item, spider):
        sql = "INSERT INTO weibocn(text_fanart,text_transfrom,comment,`like`,transmit,`time`,`from`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        print('==================================')
        self.cursor.execute(sql,(item['text_fanart'],item['text_transfrom'],item['comment'],item['like'],item['transmit'],item['time'],item['_from']))
        self.conn.commit()
        return item
    #关闭sqldb
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()