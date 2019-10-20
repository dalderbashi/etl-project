# Soybean Prices Analysis ETL Pipeline

This repository represents an Extract, Transform, and Load (ETL) pipeline for soybean prices analysis. The purpose of this project is to transform and load data in a format that will allow one to then analyze the effects of factors such as climate and fuel on soybean prices. 
 
Additionally, we were also interested in seeing the impact of recent “China-United States trade war” on the price of a product affected by these tariffs such as soybean.  The tariffs wars started in early 2018 and accelerated in 2019. On June 1, 2019 China imposed tariffs on 128 products it imports from America, including aluminum, airplanes, cars, pork, and soybeans (25% tariff), as well as fruit, nuts, and steel piping (15% tariff). On September 1, 2019 China began imposing additional tariffs on some of the goods. This includes a five percent tariff on US crude oil and U.S. soybeans, already subject to a 25% Chinese tariff, was hit with an extra 5% tariff on September 1, 2019, while beef and pork from the United States will get an extra 10% tariff. This came as a response to tariffs imposed by the US on a range of Chinese goods. (sources: https://www.china-briefing.com/news/the-us-china-trade-war-a-timeline/ , 
https://www.reuters.com/article/us-usa-trade-tariffs-factbox/factbox-next).
 
We downloaded climate data from NOAA Climate Data Center  for the states of Iowa and Illinois and soybean and crude oil daily prices from investing.com in csv format. We transformed the climate data by dropping any null values and limited the columns to: date, precipitation and temperature. Then we grouped climate data by date and averaged temperature and precipitation values. We calculated the average daily price for soybean and crude oil data and limited the columns to: date, daily open price and daily average price. Transformed csv files then were written to the output folder. The data was then loaded into PostgreSQL with date being a primary key for the 4 tables  via the sqlalchemy package. 
 
We ran into issues downloading the csvs from the NOAA Climate Data Center whereby  the allowable max size is 1GB for a single pull. We ended up with multiple climate csv files for each state. We used the glob method to merge multiple csvs together to create on data frame.  The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order. No tilde expansion is done, but *, ?, and character ranges expressed with [] will be correctly matched. This is done by using the os.listdir() and fnmatch.fnmatch() functions in concert, and not by actually invoking a subshell.


## Data Sources
* NOAA Climate Data Center (https://www.ncdc.noaa.gov/cdo-web/search)  
From NOAA we extracted csv files of climate data including station, station name, date, perception, and temperature. The data represented daily values from 1/1/2014 to 9/30/2019 for the precipitation and temperature observations in the states of Illinois and Iowa. We chose to focus on climate in Illinois and Iowa as these are the top two soybean  producing states in the nation. Illinois produced the most soybeans (698.7 million bushels) of any state in the nation last year and was runner-up to Iowa in total corn production with 2.27 billion bushels.(sourcehttps://farmweeknow.com/story-official-illinois-corn-soybean-yields-set-records-0-185998)

* https://www.investing.com/  
From investing.com we obtained the daily prices for soybean as measured by  US soybeans futures contracts price and the daily prices for crude oil as measured by crude oil WTI futures contracts price. We queried the data for daily soybean and oil prices from investing.com starting from 1/1/2010 to 10/14/2019, however data was returned a few days after 1/1/2010 with missing data over the weekends and holidays as no trading occurs on these days. 

## Pipeline
1. Download data files
     * Submit request to NOAA Climate Data Center for daily weather station data in Illinois from 1/1/2014 to 9/30/2019. Receive csv files in email in either a six month or one year increments due to max size allowance of 1GB for a single pull. Repeat the same process for climate data in the state of Iowa. 
     * Download daily soybean and oil prices from investing.com starting from 1/1/2010 to 10/14/2019 in a csv format. Note that the data was returned a few days after 1/1/2010 with missing data over the weekends and holidays as no trading occurs on these days. 
     * See csv files in the input folder.

2. Transformations
     * Illinois Weather `src/transforms/illinois.py`
          * Load source weather data (1,259,052 records)
          * Used the glob method to join 12 csvs together. 
          * Dropped rows with no data for TOBS and PRCP and ended up with (228,578 records). 
          * Converted DATE column from a string to a date datatype
          * Filter columns ("date", "illinois_precip", "illinois_temp")
          * GroupBy date and get average of precipitation and temperature. 
          * Store Illinois Weather - `output/illinois_transformed`
     * Iowa Weather `src/transforms/iowa.py`
          * Load source weather data (641,580 records)
          * Used the glob method to join 6 csvs together. 
          * Dropped rows with no data for TOBS and PRCP and ended up with  (235,615 records) 
          * Converted  DATE column from a string to a date datatype
          * Filter columns ("date", "iowa_precip", "iowa_temp")
          * GroupBy date and get average of precipitation and temperature. 
          * Store Iowa Weather `output/iowa_transformed`
     * Crude Oil Prices `src/transforms/crudeoil.py`
          * Load source crude oil data (2,536 records)
          * Calculate the daily average price of crude oil by using high and low prices of the day and add the average price as a new column 
          * Converted  Date column from a string to a date datatype
          * Filter columns ("date", "crude _open_price", "crude_avg_price")
          * Format crude_avg_price to two decimal places
          * There were no null values  
          * Store crude oil prices - `output/crude_oil_transformed`
     * Crude Oil Prices `src/transforms/crudeoil.py`
          * Load source soybean data (2,638 records)
          * Format the price data to floats 
          * Calculate the daily average prices by using high and low prices of the day and add the average price as a new column
          * Converted Date column from a string to a date datatype
          * Filter columns ("date", "soybean _open_price", "soybean_avg_price")
          * There were no null values  
          * Store soybean prices - `output/soybean_transformed`


3. Load
   * Schema - `sql/schema/schema.sql`
   * Data - `src/load.py`
     * Soybean Prices
     * Crude Oil Prices
     * Illinois Weather
     * Iowa Weather


