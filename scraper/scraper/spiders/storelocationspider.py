# -*- coding: utf-8 -*-
import MySQLdb
import scrapy




class StorelocationspiderSpider(scrapy.Spider):


    name = 'storelocationspider'
    allowed_domains = ['tesco.com']
    start_urls = []
    start = 0
    end = 0
    db = 0

    def __init__(self):
        super(StorelocationspiderSpider, self)
        self.logger.debug('Start: ' + str(self.start))
        self.logger.debug('End: ' + str(self.end))
        self.logger.debug('db: ' + str(self.db))
        self.logger.debug("Tesco spider initialised")


    @classmethod
    def setInitialVariables(cls, start, end, db):
        cls.start = start
        cls.end = end
        cls.db = db

    def start_requests(self):
        self.logger.debug('Tesco spider start_requests function')
        for i in range(int(self.start), int(self.end)):
            url = 'http://www.tesco.com/store-locator/uk/?bID=%s' % str(i)
            self.logger.debug('Spider requesting : %s', url)
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        for store_response in response.css('body #content'):
            storename = store_response.css('.store-details .store-name::text').get()
            if storename is not None:
                yield{
                    'storeID': store_response.css('.store-details .store-name').attrib["title"],
                    'storeName': storename,
                    'address': store_response.css('.store-details .address .text::text').get(),
                    'telephone': store_response.css('.store-details .phone-number .text::text').get()
                }

