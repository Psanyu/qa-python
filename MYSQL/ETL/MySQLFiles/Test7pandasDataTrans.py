import mysql.connector
import pandas as pd
import os

conn = mysql.connector.connect(option_files='C:/Users/pandi/QuerySurge/.my.cnf')
curpath=os.getcwd()
file4='CitiesL.csv'
filepath4=os.path.join(curpath, '../DataFiles', file4)

query = """ Select * from city_house_prices"""

df= pd.read_sql(query,conn)

df.set_index('Date',inplace=True)
df = df.stack().reset_index()
df.columns=['dates', 'city', 'prices']

df.to_csv(filepath4)

conn.close()