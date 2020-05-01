
### Status
[![Build Status](https://travis-ci.com/milror00/TescoStoreLocationScraper.png)](https://travis-ci.com/milror00/TescoStoreLocationScraper.svg?branch=master)

# Tesco Store Location Scraper

This is a demo project that uses python - and scrapy to scrape tesco's published stored locations.

This is a demo to demonstrate the skills I have for scraping. This code is not to be used for any reason commercial or personally other than to demonstrate the approach to scraping.

Requirements to run :

* Python 3.7 above
* scrapy 2.1.0



Steps for installation:

1. Clone git repo
1. pip install -r requirements.txt
1. run scrapy crawl storelocationspider -o stores.jl -a start=3038 -a end=3045 -db=1
(the start end refer to the storeID, db 0 = no db stdout 1 = use mysql db in vagrant)

# vagrant

To use vagrant do :

1. Install vagrant
1. Vagrant up 
1. In a terminal : vagrant ssh
1. sudo nano /etc/mysql/my.cnf change: bind-address = 0.0.0.0
1. Ctrl-x , y 
1. Restart mysql : sudo /etc/init.d/mysql restart
1. connect to mysql : username vagrant password : password host: 127.0.0.1


# Results - for Stdout
The results can be found in the stores.jl file located in /storelocator

Valid Stores:

|Store ID |Store Name                             |Address                                |Telephone |
|---------|---------------------------------------|---------------------------------------|---------------|
|3038    |Polegate Esso Express                   |94 Eastbourne Rd, Polegate, BN26 5DD                        |0345 677 9549 | 
|3039    |Plymouth Transit Way Superstore         |Transit Way, Plymouth, PL5 3TW                              |0345 677 9550 |
|3040    |Poole Fleets Corner Extra               |Waterloo Rd, Poole, BH17 7EJ                                |0345 677 9551 | 
|3041    |Prestwich Superstore                    |Valley Park Rd, Prestwich, Manchester, M25 3TG              |0345 677 9552 | 
|3045    |Princes Risborough Superstore           |Longwick Rd, Princes Risborough, HP27 9TS                   |0345 677 9553 | 



