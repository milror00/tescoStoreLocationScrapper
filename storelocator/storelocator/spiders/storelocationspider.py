# -*- coding: utf-8 -*-
import scrapy


class StorelocationspiderSpider(scrapy.Spider):
    name = 'storelocationspider'
    allowed_domains = ['http://www.tesco.com']
    start_urls = ['http://http://www.tesco.com/']

    def __init__(self, start=0, end=0, *args, **kwargs):
        super(StorelocationspiderSpider, self).__init__(*args, **kwargs)
        self.start = int(start)
        self.end = int(end)

    def start_requests(self):
        for i in range(self.start, self.end):
            url = 'http://www.tesco.com/store-locator/uk/?bID=%s' % str(i)
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for store_response in response.css('body #content'):
            storename = store_response.css('.store-details .store-name::text').get()
            if storename is not None:
                yield{
                    'storeID': store_response.css('.store-details .store-name').attrib["title"],
                    'storeName': storename,
                    'address': store_response.css('.store-details .address .text::text').get(),
                    'telephone': store_response.css('.store-details .phone-number .text::text').get()
                }

