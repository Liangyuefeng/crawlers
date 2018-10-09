# -*- coding: utf-8 -*-
import scrapy
from recommend.items import RecommendItem
from scrapy.http import Request

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    def start_requests(self):
        ua={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}
        yield Request('https://www.douban.com/tag/%E7%A8%8B%E5%BA%8F%E5%91%98/book',headers=ua)

    def parse(self, response):
        item=RecommendItem()
        item['title']=response.xpath("//a[@class='title']/text()").extract()
        # item['desc']=response.xpath("//span[@class='excerpt']/p/text()").extract()
        item['link']=response.xpath("//a[@class='title']/@href").extract()
        yield item