import mysql.connector
import pandas as pd

conn = mysql.connector.connect(option_files='C:/Users/pandi/QuerySurge/.my.cnf')
query = "SELECT title,year FROM imdb_movies WHERE year between 2005 and 2008"
df= pd.read_sql(query,conn)

year = df['year']==2006
yearn = df[~year]

print(df.head())

print(year)

print(yearn.head())

conn.close()