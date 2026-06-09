import mysql.connector
import pandas as pd


conn = mysql.connector.connect(option_files='C:/Users/pandi/QuerySurge/.my.cnf')
query = "SELECT title,year,genre FROM imdb_movies LIMIT 15"
df= pd.read_sql(query,conn)
print(df.head())
print(df.info())
print(df.describe())
print(df.describe(include='all'))
print(df.dtypes())

conn.close()