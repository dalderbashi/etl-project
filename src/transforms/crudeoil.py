#!/usr/bin/env python
# coding: utf-8

# ## Extract, Transform and Load


import pandas as pd
from sqlalchemy import create_engine
import datetime as dt


#read data file
crudeoil_file = "./input/crudeoil/Crude Oil WTI Futures Historical Data.csv"
crudeoil_df = pd.read_csv(crudeoil_file)
#crudeoil_df.head()

#identifying data types
#crudeoil_df.dtypes


# ### Transform premise DataFrames

#calculate the average price for the day using high and low prices
#add the new values into the column
crudeoil_df["Crude_Avg_Price"] = crudeoil_df[['High','Low']].mean(axis=1)
#crudeoil_df.head()

#format date column into date type
crudeoil_df['Date'] =  pd.to_datetime(crudeoil_df['Date'],format='%d-%b-%y')
#crudeoil_df['Date']

#crudeoil_df.dtypes

# Create a filtered dataframe from specific columns
crudeoil_cols = ["Date", "Open","Crude_Avg_Price"]
crudeoil_transformed= crudeoil_df[crudeoil_cols].copy()


# Rename the column headers
crudeoil_transformed = crudeoil_transformed.rename(columns={"Open": "crude_open_price", "Date":"date",
 "Crude_Avg_Price":"crude_avg_price"})
#crudeoil_transformed.head()

#format crudeoil_avg_price to two decimal place
crudeoil_transformed=crudeoil_transformed.round({'crude_avg_price': 2})
#crudeoil_transformed.head()


crudeoil_transformed.to_csv('./output/crude_oil_transformed.csv', index=False)
