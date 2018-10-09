# -*- coding: utf-8 -*-
import scrapy
from recommend.items import RecommendItem
from scrapy.http import Request

class FunrecomSpider(scrapy.Spider):
    name = 'funrecom'
    allowed_domains = ['douban.com']
    def start_requests(self):
        ua={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}
        yield Request('https://movie.douban.com/chart',headers=ua)

    def parse(self, response):
        item=RecommendItem()
        item['title']=response.xpath("//div[@ class='name']/a/text()").extract()
        item['link']=response.xpath("//div[@ class='name']/a/@href").extract()
        yield item
