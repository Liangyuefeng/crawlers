# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TsPipeline(object):
    def process_item(self, item, spider):
        print(item["title"])
        print(item["link"])
        print(item["stu"])
        print("-----------")
        return item
