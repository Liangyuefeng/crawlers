# -*- coding: utf-8 -*-
import scrapy
from csdn.items import CsdnItem
from scrapy.http import Request


class DatabaseSpider(scrapy.Spider):
    name = 'database'
    allowed_domains = ['jobbole.com']


    def start_requests(self):
        ua={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}
        yield Request('http://blog.jobbole.com/tag/database/',headers=ua)

    def parse(self, response):
        item=CsdnItem()
        item['title']=response.xpath("//a[@class='archive-title']/text()").extract()
        item['desc']=response.xpath("//span[@class='excerpt']/p/text()").extract()
        item['link']=response.xpath("//a[@class='archive-title']/@href").extract()
        item['time']=response.xpath("//dd[@class='time']/text()").extract()
        yield item
