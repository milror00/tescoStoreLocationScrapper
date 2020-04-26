import lxml
import requests
import urllib3
from io import BytesIO
from lxml import etree
from lxml import html
import logging

class TescoLocationScraper():

    def __init__(self):
        logging.getLogger("urllib3").setLevel(logging.WARNING)
        self.start = 0
        self.finish = 0
        self.invalidStoreID = []
        self.stores = []
        self.url = 'http://www.tesco.com/store-locator/uk/?bID={}'

    def getURL(self, url ):
        http = urllib3.PoolManager()
        self.response = http.request('GET', url)

    def getStorLocation(self,url, storeID):
        details = {}
        self.getURL(url)
        dom = lxml.html.parse(BytesIO(self.response.data))
        xpatheval = etree.XPathDocumentEvaluator(dom)
        error = xpatheval('.//*[@class="error"]')
        if len(error) != 0:
            return False
        details['storeName'] = xpatheval('.//*[@class="store-name"]')[0].text
        details['address'] = xpatheval('.//*[@itemprop="streetAddress"]')[0].text
        details['telephone'] =  xpatheval('.//*[@itemprop="telephone"]')[0].text
        details['storeID'] = str(storeID)
        self.stores.append(details)
        return True

    def iterate_through_tesco_store_pages(self, start, finish):
        while start <= finish:
            details = {}
            formatted_url = self.url.format(str(start))
            if not self.getStorLocation(formatted_url, start):
                details['storeID'] = start
                self.invalidStoreID.append(details)
            start = start + 1
        return self.stores, self.invalidStoreID

if __name__ == '__main__':
    scraper = TescoLocationScraper()
    stores,invalidStores = scraper.iterate_through_tesco_store_pages(3038,3045)
    print('Valid Stores:')
    print('|Store ID     |Store Name      |Address      |Telephone |')
    print('|---------|---------------------------------------|---------------------------------------|---------------|')
    for store in stores:
        print('|{0: <8}|{1: <40}|{2: <60}|{3: <15}'.format(
              store['storeID'],
              store['storeName'],
              store['address'],
              store['telephone']))
    print('Invalid StoreIDs :')
    for invalid_store in invalidStores:
        print('{0: <8}'.format(
        invalid_store['storeID'],))