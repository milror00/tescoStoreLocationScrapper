import lxml
import requests
import urllib3
from io import BytesIO
from lxml import etree
from lxml import html


class TescoLocationPage():

    def __getURL__(self, context):
        http = urllib3.PoolManager()
        context.response = http.request('GET', context.currentURL)

    def getStorLocation(self, context, storeID):
        details = {}
        self.__getURL__(context)
        dom = lxml.html.parse(BytesIO(context.response.data))
        xpatheval = etree.XPathDocumentEvaluator(dom)
        error = xpatheval('.//*[@class="error"]')
        if len(error) != 0:
            return False
        details['storeName'] = xpatheval('.//*[@class="store-name"]')[0].text
        details['address'] = xpatheval('.//*[@itemprop="streetAddress"]')[0].text
        details['telephone'] =  xpatheval('.//*[@itemprop="telephone"]')[0].text
        details['storeID'] = str(storeID)
        context.stores.append(details)
        return True




