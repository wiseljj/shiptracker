# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShiptrackerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    Ship_name_en=scrapy.Field()
    MMSI=scrapy.Field()
    IMO=scrapy.Field()
    Call_sign=scrapy.Field()
    Latitude=scrapy.Field()
    Nationality=scrapy.Field()
    Longitude=scrapy.Field()
    Heading=scrapy.Field()
    Ship_type=scrapy.Field()
    Track=scrapy.Field()
    Route_state=scrapy.Field()
    Ship_speed=scrapy.Field()
    Ship_length=scrapy.Field()
    Scheduled_port=scrapy.Field()
    Ship_width=scrapy.Field()
    Scheduled_time=scrapy.Field()
    Draft=scrapy.Field()
    Turnover_time=scrapy.Field()
    Ship_Chinese_name=scrapy.Field()
    Gross_ton=scrapy.Field()
    Deadweight_ton=scrapy.Field()
    Shipowner=scrapy.Field()


