import mysql.connector
import pandas as pd
import os

conn = mysql.connector.connect(option_files='C:/Users/pandi/QuerySurge/.my.cnf')
curp=os.getcwd()
file2='MoviesList.csv'
filepath2=os.path.join(curp, '../DataFiles', file2)

query = "SELECT title,year,"\
        " CASE"\
        " WHEN year < 2007 THEN 'Good'"\
        " WHEN year = 2007 THEN 'Okay'"\
        " WHEN year > 2007 THEN 'Bad'"\
        " END as oldmovies"\
        " FROM imdb_movies"\
        " WHERE year between 2005 and 2008"\
        " LIMIT 11"



df= pd.read_sql(query,conn)

year = df['year']==2006
yearn = df[~year]

print(df.head())

print(year)

print(yearn.head())

df.to_csv(filepath2)

conn.close()