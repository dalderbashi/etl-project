#!/usr/bin/env python
# coding: utf-8

# ## Homework #13: Extract-Transform-Load 
# Purpose of our ETL is to prepare data sets to answer the question:
#      *Is the price of soybeans dependent on global fuel prices or weather in top-producing states of Iowa and Illinois?*



# Import libraries for use in Python programs
import pandas as pd
from sqlalchemy import create_engine
import datetime as dt


# ###  Extraction step of our ETL project:
# * Submit request to NOAA Climate Data Center for weather station data in Illinois for the years 2014 to 2019
# * Receive CSV files in email in either six month or one year increments due to max size allowance of 1GB for a single pull
# * Concatenate all of the files into one large DataFrame using "glob" method

# >**What is import glob?**
# > An asterisk (*) matches zero or more characters in a segment of a name. For example, dir/*. import glob for name in glob. > > > glob('dir/*'): print name. The pattern matches every pathname (file or directory) in the directory dir, without recursing > > > further into subdirectories.



import glob
import numpy as np

illinois_df = pd.concat(map(pd.read_csv, glob.glob("./input/illinois/*.csv")))
#illinois_df.count()

illinois_df = illinois_df[(~np.isnan(illinois_df.TOBS)) & (~np.isnan(illinois_df.PRCP))]


#print(len(illinois_df))

#illinois_df.head()

#illinois_df.tail()


# What are the data types in the DataFrame
#illinois_df.dtypes


## Convert "Date" from a string to a date-time-group variable
illinois_df["DATE"] =  pd.to_datetime(illinois_df["DATE"])
#illinois_df.dtypes



# Rename the column headers
illinois_df = illinois_df.rename(columns={"DATE": "Date",
                                                          "PRCP": "Illinois_Precip",
                                                          "TOBS": "Illinois_Temp"})
#illinois_df.head()


illinois_transformed = illinois_df.groupby(['Date']).mean()
#illinois_transformed


#print(len(illinois_transformed))


illinois_transformed.to_csv("./output/illinois_transformed.csv")

