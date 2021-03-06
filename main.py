import sys
import argparse

from scraper.run_scraper import Scraper
from scraper.scraper.spiders.storelocationspider import StorelocationspiderSpider


class ScraperMain():

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--start')
        parser.add_argument('--end')
        args = parser.parse_args()
        scraper = Scraper()
        StorelocationspiderSpider.setInitialVariables(args.start, args.end)
        scraper.run_spiders()

if __name__ == "__main__":
   main = ScraperMain()
   main.main()

