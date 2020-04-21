# Created by Oem at 21/04/2020
Feature:
Feature: As a researcher I need to gather all the Tesco locations
         so I can store them for further research

  Scenario: Scrape a range of storeID's if a store exists for the ID then store the location information otherwise store invalid store id continue to next ID write out locations in a csv file or write to std output


    Given I have a range of store IDs from 3038 to 3045
    And I retrieve the location details
    Then I write out locations to the std output

