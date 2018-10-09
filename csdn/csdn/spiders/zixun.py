# -*- coding: utf-8 -*-
import scrapy
from csdn.items import CsdnItem
from scrapy.http import Request

class ZixunSpider(scrapy.Spider):
    name = 'zixun'
    allowed_domains = ['csdn.net']
    # start_urls = ['https://www.csdn.net/nav/news/']

    def start_requests(self):
        ua={"User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}
        yield Request('https://blog.csdn.net/',headers=ua)

    def parse(self, response):
        item=CsdnItem()
        item['title']=response.xpath("//h2[@class='csdn-tracking-statistics']"
                                     "/a[@strategy='career']/text()").extract()
        item['desc']=response.xpath("//div[@class='summary oneline']/text()").extract()
        item['link']=response.xpath("//h2[@class='csdn-tracking-statistics']"
                                    "/a[@strategy='career']/@href").extract()
        item['time']=response.xpath("//dd[@class='time']/text()").extract()
        yield item

