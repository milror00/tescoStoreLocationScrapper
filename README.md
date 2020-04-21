# Tesco Store Location Scrapper

This is a demo project that uses python - request and behave to scrape tesco's published stored locations.

This is a demo to demonstrate the skills I have for scraping. This code is not to be used for any reason commercial or personally other than to demonstrate the approach to scraping.

Requirements to run :

Python 3.7 above

behave==1.2.6

requests==2.23.0

lxml==4.5.0

idna==2.9

urlib3==1.25.9


Steps for installation:

1. Clone git repo
2. I use PyCharm Professional to I import the project which creates a virtual environment for the project
3. Install libraries :
  pip install behave
  pip install requests
  pip install lxml
  
4. Open the console at the root of project and run the command :

behave ./features

# Feature 

Feature: As a researcher I need to gather all the Tesco locations

         so I can store them for further research

  Scenario: Scrape a range of storeID's if a store exists for the ID then store the location information otherwise store invalid store id continue to next ID write out locations in a csv file or write to std output


    Given I have a range of store IDs from 3038 to 3045
    
    And I retrieve the location details
    
    Then I write out locations to the std output
    
    Output:
    
3038
Polegate Esso Express
94 Eastbourne Rd, Polegate, BN26 5DD
0345 677 9549

3039
Plymouth Transit Way Superstore
Transit Way, Plymouth, PL5 3TW
0345 677 9550

3040
Poole Fleets Corner Extra
Waterloo Rd, Poole, BH17 7EJ
0345 677 9551

3041
Prestwich Superstore
Valley Park Rd, Prestwich, Manchester, M25 3TG
0345 677 9552

3045
Princes Risborough Superstore
Longwick Rd, Princes Risborough, HP27 9TS
0345 677 9553

Process finished with exit code 0

    



