class Configuration:

    def getEnvironment(self):
        return 'LIVE'

    def getBrowserType(self):
        return 'FIREFOX'


    def getURL(self):
        return 'http://www.tesco.com/store-locator/uk/?bID={}'

    def getTimeOut(self):
        return 10
