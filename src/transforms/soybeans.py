#!/usr/bin/env python
# coding : utf - 8

## Load and Transform Soybean Data

import pandas as pd
from sqlalchemy import create_engine
import datetime as dt
import os

#home_dir = os.getcwd()
#soybean_file_test_path = os.path.join(home_dir, '/input/soybean/US Soybeans Futures Historical Data.csv')

### Extract CSVs into DataFrames

soybean_file = "./input/soybean/US Soybeans Futures Historical Data.csv"
#convert csv to data frame and convert column values to float
soybean_df = pd.read_csv(soybean_file, thousands = ',', decimal = '.')
#soybean_df.head()


### Transform Soybean DataFrame

#convert date from object to a date
soybean_df['Date'] = pd.to_datetime(soybean_df['Date'], format = '%d-%b-%y')

#soybean_df.dtypes
#calculate average soybean price and add it as a new column sing high and low values
soybean_df["soybean_avg_price"] = soybean_df[["High", "Low"]].mean(axis = 1)
#soybean_df.head()

# Create a filtered dataframe from specific columns
soybean_cols = ["Date", "Open", "soybean_avg_price"]
soybean_transformed = soybean_df[soybean_cols].copy()

# Rename the column headers
soybean_transformed = soybean_transformed.rename(columns = {
    "Open": "Soybean_Open_Price",
    "soybean_avg_price": "Soybean_Avg_Price"
})
#soybean_transformed.count()
#soybean_transformed.head()


#export to csv
soybean_transformed.to_csv("./output/soybean_transformed.csv", index = False)
