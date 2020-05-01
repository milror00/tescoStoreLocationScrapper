import sys
import argparse

from scraper.run_scraper import Scraper
from scraper.scraper.spiders.storelocationspider import StorelocationspiderSpider


class ScraperMain():

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--start')
        parser.add_argument('--end')
        parser.add_argument('--usedb')
        args = parser.parse_args()
        scraper = Scraper()
        StorelocationspiderSpider.setInitialVariables(args.start, args.end, args.usedb)
        scraper.run_spiders()

if __name__ == "__main__":
   main = ScraperMain()
   main.main()

