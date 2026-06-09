import mysql.connector
import pandas as pd
import os

conn = mysql.connector.connect(option_files='C:/Users/pandi/QuerySurge/.my.cnf')
currpath = os.getcwd()

file='MySQL.csv'
filepath= os.path.join(currpath, '../DataFiles', file)

print(filepath)

query = "SELECT title,year FROM imdb_movies WHERE year between 2005 and 2008"
df= pd.read_sql(query,conn)

year = df['year']==2006
yearn = df[~year]

print(df.head())

print(year)

print(yearn.head())

os.makedirs(os.path.dirname(filepath), exist_ok=True)

df.to_csv(filepath)


conn.close()