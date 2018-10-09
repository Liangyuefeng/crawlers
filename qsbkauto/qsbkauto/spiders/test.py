# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qsbkauto.items import QsbkautoItem
from scrapy.http import Request


class TestSpider(CrawlSpider):
    name = 'test'
    allowed_domains = ['qiushibaike.com']
# start_urls = ['http://qiushibaike.com/']

##链接提取规律
    rules = (
        Rule(LinkExtractor(allow='article'), callback='parse_item', follow=True),
    )
##第一次爬取url设置
    def start_requests(self):
        ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}
        yield Request('http://qiushibaike.com/text/', headers=ua)

    def parse_item(self, response):
        i = QsbkautoItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i["content"] = response.xpath("//div[@class='content']/text()").extract()
        i["link"] = response.xpath("//link[@rel='canonical']/@href").extract()
        print(i["content"])
        print(i["link"])
        print("")
        return i
