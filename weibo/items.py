# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    text_fanart = scrapy.Field()    #原创
    text_transfrom = scrapy.Field() #转发内容
    comment = scrapy.Field()    #评论数
    like = scrapy.Field()   #点赞数
    transmit = scrapy.Field()   #转发数
    time = scrapy.Field()   #发表时间
    _from = scrapy.Field()    #来自的客户端