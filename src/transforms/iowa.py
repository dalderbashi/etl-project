#!/usr/bin/env python
# coding: utf-8

# # Homework #13: Extract-Transform-Load
# Purpose of our ETL is to prepare data sets to answer the question: Is the price of soybeans dependent on global fuel prices or weather in top-producing states of Iowa and Illinois?
# 
# >**What is import glob?**
# > An asterisk (*) matches zero or more characters in a segment of a name. For example, dir/*. import glob for name in glob. > > > glob('dir/*'): print name. The pattern matches every pathname (file or directory) in the directory dir, without recursing > > > further into subdirectories.

import pandas as pd
from sqlalchemy import create_engine
import datetime as dt
# #### Extract CSVs into DataFrames
import glob
import numpy as np
import os

#iowa_df = pd.concat(map(pd.read_csv, glob.glob("/iowa*.csv")))
iowa_df = pd.concat(map(pd.read_csv, glob.glob("../../input/iowa/*.csv")))
print('first load successful')
print(iowa_df.count())

iowa_df.head()
iowa_df.tail()
iowa_df = iowa_df[(~np.isnan(iowa_df.TOBS)) & (~np.isnan(iowa_df.PRCP))]
# print(len(iowa_df))
iowa_df.head()

## Convert "Date" from a string to a date-time-group variable
iowa_df["DATE"] =  pd.to_datetime(iowa_df["DATE"])
iowa_df.dtypes
# Rename the column headers
iowa_df = iowa_df.rename(columns={"DATE": "Date",
                                                          "PRCP": "Iowa_Precip",
                                                          "TOBS": "Iowa_Temp"})
iowa_df.head()
iowa_transformed = iowa_df.groupby(['Date']).mean()
iowa_transformed.head()
iowa_transformed.to_csv("../../output/iowa_transformed.csv")







