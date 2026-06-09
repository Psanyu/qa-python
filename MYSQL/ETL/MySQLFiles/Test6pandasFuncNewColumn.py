import mysql.connector
import pandas as pd
import os

conn = mysql.connector.connect(option_files='C:/Users/pandi/QuerySurge/.my.cnf')
curp=os.getcwd()
file3='MoviesL.csv'
filepath3=os.path.join(curp, '../DataFiles', file3)

query = "SELECT title,year,duration,avg_vote,"\
        " CASE"\
        " WHEN year < 2007 THEN 'old'"\
        " WHEN year = 2007 THEN 'Okay'"\
        " WHEN year > 2007 THEN 'Recent'"\
        " END as moviestype"\
        " FROM imdb_movies"\
        " WHERE year between 2005 and 2008"\
        " LIMIT 11"

def moviedur(t):
    if t < 60:
        return 'Short Movie'
    elif 60 <= t <= 150:
        return 'Regular Length Movie'
    elif t > 150:
        return 'Long Movie'
    else:
        return 'No Movie'

df= pd.read_sql(query,conn)

df['movieselection']=df['duration'].apply(moviedur)


year = df['year']==2006
yearn = df[~year]

print(df.head())

print(year)

print(yearn.head())

df.to_csv(filepath3)

conn.close()