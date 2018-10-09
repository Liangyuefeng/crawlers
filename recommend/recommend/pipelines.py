# -*- coding: utf-8 -*-
import pymysql

# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class RecommendPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host='localhost', user='root', passwd='lyf2818233', db='datablog',
                               charset='utf8')
        cur = conn.cursor()  # 获取一个游标

        for i in range(0, len(item['title'])):
            title = item['title'][i].strip()
            # desc = item['desc'][i].strip()
            link = item['link'][i]

            sql = "insert into blog_csdnrecommend(`title`,`link`) values ('" + title + "' ,'" + link + "')"
            cur.execute(sql)  # 执行插入

            conn.commit()
        conn.close()

        return item
