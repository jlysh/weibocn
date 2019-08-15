# -*- coding: utf-8 -*-
from random import Random

import scrapy
from weibo.items import WeiboItem
from datetime import datetime
from datetime import timedelta

class WeibocnSpider(scrapy.Spider):
    name = 'weibocn'
    allowed_domains = ['weibo.cn']
    url = 'https://weibo.cn/u/1792951112?page={page}'

    # start_urls = ['https://weibo.cn/u/1792951112']

    def transform(self, cookies):
        cookie_dict = {}
        cookies = cookies.replace(' ', '')
        list = cookies.split(';')
        for i in list:
            keys = i.split('=')[0]
            values = i.split('=')[1]
            cookie_dict[keys] = values
        return cookie_dict

    # Override start_requests()
    # 此方法相当于 requests.get()方法
    def start_requests(self):
        for page in range(1, 65):
            yield scrapy.Request(url=self.url.format(page=page), callback=self.parse)

    # 此方法中的response相当于response = requests.get()
    def parse(self, response):
        # print(response.text)
        item = WeiboItem()
        for p in response.xpath("//div[@class='c'and @id]"):
            try:
                text_transfrom = "".join(p.xpath("./div/text()").re(r'[\u4e00-\u9fa5]'))
                text_fanart = "".join(p.xpath("./div/span[@class='ctt']/text()").extract())
                item['text_fanart'] = text_fanart
                item['text_transfrom'] = text_transfrom
                item['like'] = "".join(p.xpath("./div/a").re(r'赞\[[0-9]*?\]')).replace('赞[', '').replace(']', '')
                item['transmit'] = "".join(p.xpath("./div/a").re(r'转发\[[0-9]*?\]')).replace('转发[', '').replace(']', '')
                item['comment'] = "".join(p.xpath("./div/a").re(r'评论\[[0-9]*?\]')).replace('评论[', '').replace(']', '')
                time_from = "".join(p.xpath("./div/span[@class='ct']/text()").extract()).split("\xa0来自")
                item['time'] = self.clear_date(time_from[0])
                item['_from'] = time_from[1]
                yield item
            except Exception as e:
                print(e)
                continue


    def clear_date(self,publish_time):
        if "刚刚" in publish_time:
            publish_time = datetime.now().strftime('%Y-%m-%d %H:%M')

        elif "分钟" in publish_time:
            minute = publish_time[:publish_time.find("分钟")]
            minute = timedelta(minutes=int(minute))
            publish_time = (
                    datetime.now() - minute).strftime(
                "%Y-%m-%d %H:%M")
        elif "今天" in publish_time:
            today = datetime.now().strftime("%Y-%m-%d")
            time = publish_time.replace('今天', '')
            publish_time = today + " " + time

        elif "月" in publish_time:
            year = datetime.now().strftime("%Y")
            publish_time = str(publish_time)

            publish_time = year + "-" + publish_time.replace('月', '-').replace('日', '')
        else:
            publish_time = publish_time[:16]

        return publish_time