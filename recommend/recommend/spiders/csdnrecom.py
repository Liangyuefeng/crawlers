# -*- coding: utf-8 -*-
import scrapy
from recommend.items import RecommendItem
from scrapy.http import Request

class CsdnrecomSpider(scrapy.Spider):
    name = 'csdnrecom'
    allowed_domains = ['douban.com']
    def start_requests(self):
        ua={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}
        yield Request('https://music.douban.com/tag/%E5%91%A8%E6%9D%B0%E4%BC%A6',headers=ua)

    def parse(self, response):
        item=RecommendItem()
        item['title']=response.xpath("//div[@class='pl2']/a/text()").extract()
        item['link']=response.xpath("//div[@class='pl2']/a/@href").extract()
        yield item
