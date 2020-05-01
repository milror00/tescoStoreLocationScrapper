
### Status
[![Build Status](https://travis-ci.com/milror00/TescoStoreLocationScraper.png)](https://travis-ci.com/milror00/TescoStoreLocationScraper.svg?branch=master)

# Tesco Store Location Scraper

This is a demo project that uses python - and scrapy to scrape tesco's published stored locations.

This is a demo to demonstrate the skills I have for scraping. This code is not to be used for any reason commercial or personally other than to demonstrate the approach to scraping.

Requirements to run :

* Python 3.7 above
* scrapy 2.1.0



## Steps for installation:

1. Clone git repo
1. pip install -r requirements.txt
1. settings file is by default set to write out results into a json file data_export.json.
1. run python main.py --start 3038 --end 3045. This is the page range - to search for stores
1. In the root of the file you should find data_export.json

## Troubleshooting 

Logs are streamed to stdout - exceptions and errors will be captured there please red through the log  

Log Level are set in the settings.py:

```
#LOG_FILE = 'scrapy.log'
LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'
LOG_ENCODING = 'utf-8'
LOG_STDOUT =True

```

# vagrant

To use vagrant do :

1. Install vagrant
1. Vagrant up 
1. In a terminal : vagrant ssh
1. sudo nano /etc/mysql/my.cnf change: bind-address = 0.0.0.0
1. Ctrl-x , y 
1. Restart mysql : sudo /etc/init.d/mysql restart
1. connect to mysql : username vagrant password : password host: 127.0.0.1

## MySql setup

1. Build the vagrant machine - see above
1. Create a database named tesco

```
CREATE DATABASE tesco
```

   Create stores table DDL below


```
create table stores
(
	id int auto_increment,
    storeID int not null,
	storeName varchar(200) not null,
	address varchar(200) not null,
	telephone varchar(40) null,
	constraint stores_pk
		primary key (id)
);

create index stores_storeName_index
	on stores (storeID desc);

create index stores_storeName_index
	on stores (storeID desc);

commit;

```

 Change the settings.py : see below

```
ITEM_PIPELINES = {
    'scraper.scraper.json_item_pipeline.JsonTescoPipeline': 300,
}

to

ITEM_PIPELINES = {
    'scraper.scraper.mysql_item_pipleine.JsonTescoPipeline': 300,
}
``` 

1. The db default connection settings are set in settings.py:

```

DB_SETTINGS = {
    'db': "tesco",
    'user': 'vagrant',
    'passwd': 'password',
    'host': '127.0.0.1',
}

```
### Run
 
run python main.py --start 3038 --end 3045



# Results

Valid Stores:

|Store ID |Store Name                             |Address                                |Telephone |
|---------|---------------------------------------|---------------------------------------|---------------|
|3038    |Polegate Esso Express                   |94 Eastbourne Rd, Polegate, BN26 5DD                        |0345 677 9549 | 
|3039    |Plymouth Transit Way Superstore         |Transit Way, Plymouth, PL5 3TW                              |0345 677 9550 |
|3040    |Poole Fleets Corner Extra               |Waterloo Rd, Poole, BH17 7EJ                                |0345 677 9551 | 
|3041    |Prestwich Superstore                    |Valley Park Rd, Prestwich, Manchester, M25 3TG              |0345 677 9552 | 
|3045    |Princes Risborough Superstore           |Longwick Rd, Princes Risborough, HP27 9TS                   |0345 677 9553 | 



