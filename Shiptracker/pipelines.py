# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from pymongo import MongoClient
from Shiptracker.items import ShiptrackerItem

class ShiptrackerPipeline(object):
    def process_item(self, item, spider):
        return item

# class ShiptrackerMongoPipeline(object):
#     def open_spider(self, spider):  # 在爬虫开启的时候仅执行一次
#         if spider.name == 'ship':
#             con = MongoClient() # 实例化mongoclient
#             self.collection = con.shiptracker.datas # 创建数据库名为shiptracker,集合名为datas的集合操作对象
#
#     def process_item(self, item, spider):
#         if spider.name == 'ship':
#             self.collection.insert(dict(item)) # 此时item对象需要先转换为字典,再插入
#         # 不return的情况下，另一个权重较低的pipeline将不会获得item
#         return item

class ShiptrackerMongoPipeline(object):
    def open_spider(self, spider):  # 在爬虫开启的时候仅执行一次
        if spider.name == 'ship':
            con = MongoClient() # 实例化mongoclient
            self.collection = con.shiptracker.datas # 创建数据库名为shiptracker,集合名为datas的集合操作对象

    def process_item(self, item, spider):
        if spider.name == 'ship':
            self.collection.insert(dict(item)) # 此时item对象需要先转换为字典,再插入
        # 不return的情况下，另一个权重较低的pipeline将不会获得item
        return item

    # con = MongoClient(
        # "mongodb://root:Wiseljj2018$$@dds-2ze1c8004c4fa9f41.mongodb.rds.aliyuncs.com:3717")  # 实例化mongoclient
