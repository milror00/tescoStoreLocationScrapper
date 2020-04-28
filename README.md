
### Status
[![Build Status](https://travis-ci.com/milror00/TescoStoreLocationScraper.png)](https://travis-ci.com/milror00/TescoStoreLocationScraper.svg?branch=master)

# Tesco Store Location Scrapper

This is a demo project that uses python - request and behave to scrape tesco's published stored locations.

This is a demo to demonstrate the skills I have for scraping. This code is not to be used for any reason commercial or personally other than to demonstrate the approach to scraping.

Requirements to run :

* Python 3.7 above
* requests==2.23.0
* lxml==4.5.0
*urlib3==1.25.9



Steps for installation:

1. Clone git repo
1. pip install -r requirements.txt
1. run the script

# Results

Valid Stores:

|Store ID |Store Name                             |Address                                |Telephone |
|---------|---------------------------------------|---------------------------------------|---------------|
|3038    |Polegate Esso Express                   |94 Eastbourne Rd, Polegate, BN26 5DD                        |0345 677 9549 | 
|3039    |Plymouth Transit Way Superstore         |Transit Way, Plymouth, PL5 3TW                              |0345 677 9550 |
|3040    |Poole Fleets Corner Extra               |Waterloo Rd, Poole, BH17 7EJ                                |0345 677 9551 | 
|3041    |Prestwich Superstore                    |Valley Park Rd, Prestwich, Manchester, M25 3TG              |0345 677 9552 | 
|3045    |Princes Risborough Superstore           |Longwick Rd, Princes Risborough, HP27 9TS                   |0345 677 9553 | 

Invalid StoreIDs :

|Store ID|
|--------|
|3042    |
|3043    |
|3044    |


