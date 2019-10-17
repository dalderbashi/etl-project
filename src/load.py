
import pandas as pd
from sqlalchemy import create_engine
import datetime as dt

connection_string = "postgres:postgres@localhost:5432/soybeans_trade"
engine = create_engine(f'postgresql://{connection_string}')

#Confirm tables
print(engine.table_names())



soybean_file = "./output/soybean_transformed.csv"
crude_oil_file = "./output/crude_oil_transformed.csv"
iowa_file = "./output/iowa_transformed.csv"
illinois_file = "./output/illinois_transformed.csv"

#convert csv to data frame and convert column values to float
soybean_df = pd.read_csv(soybean_file)
crude_oil_df = pd.read_csv(crude_oil_file)
iowa_df = pd.read_csv(iowa_file)
illinois_df = pd.read_csv(illinois_file)


soybean_df.to_sql(name='soybean', con=engine, if_exists='append', index=False)
crude_oil_df.to_sql(name='crude_oil', con=engine, if_exists='append', index=False)
iowa_df.to_sql(name='iowa', con=engine, if_exists='append', index=False)
illinois_df.to_sql(name='illinois', con=engine, if_exists='append', index=False)

