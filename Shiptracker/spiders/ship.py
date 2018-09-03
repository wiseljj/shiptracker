# -*- coding: utf-8 -*-
import scrapy
import re , json,time
from Shiptracker.items import ShiptrackerItem

class ShipSpider(scrapy.Spider):
    name = 'ship'
    allowed_domains = ['chinaports.com']
    start_urls = ['http://www.chinaports.com/shiptracker/shipinit.do']

    def start_requests(self):
        formdata = {
            'method':"poszoom",
            "center_x":"129.13591002579778",
            "center_y": "35.063743840935737",
            "resolution": "150",
            "param1":"true",
            "pos":"1",
            "type":"0"
        }
        for url in self.start_urls:
            yield scrapy.FormRequest(url,formdata=formdata,callback=self.parse)

    def parse(self, response):
        # print("***********************************")
        # print(response)
        # print("!!!"*20)
        data_str=response.text
        data_str1=re.findall(r"ck\((.*)\)",data_str)
        data_dict=json.loads(data_str1[0])
        print("***********************************")
        print(len(data_dict))
        li=[]
        detail_url="http://www.chinaports.com/shiptracker/shipinit.do"
        t=time.time()
        t1=int(t*1000)
        for i in data_dict:
            li.append(i[-1])
            formdata = {
                'method': "shipInfo",
                "userid": str(i[-1]),
                "source": "0",
                "num": str(t1),
            }
            yield scrapy.FormRequest(detail_url, formdata=formdata,callback=self.parse_detail)
    def parse_detail(self,response):
        # print("^"*50)
        # print(response.text)
        # print(type(response.text))
        # pass
        data_str = response.text
        data_li = json.loads(data_str)
        # print(data_li)
        # print(type(data_li))
        item = ShiptrackerItem()
        item['Ship_name_en']=data_li[0]
        item['MMSI']=data_li[1]
        item['IMO']=data_li[2]
        item['Call_sign']=data_li[3]
        item['Latitude']=data_li[4]
        item['Nationality']=data_li[5]
        item['Longitude']=data_li[6]
        item['Heading']=data_li[7]
        item['Ship_type']=data_li[8]
        item['Track']=data_li[9]
        item['Route_state']=data_li[10]
        item['Ship_speed']=data_li[11]
        item['Ship_length']=data_li[12]
        item['Scheduled_port']=data_li[13]
        item['Ship_width']=data_li[14]
        item['Scheduled_time']=data_li[15]
        item['Draft']=data_li[16]
        item['Turnover_time']=data_li[17]
        item['Ship_Chinese_name']=data_li[18]
        item['Gross_ton']=data_li[19]
        item['Deadweight_ton']=data_li[20]
        item['Shipowner']=data_li[24]
        print(item)
        print(type(item))
        yield item









