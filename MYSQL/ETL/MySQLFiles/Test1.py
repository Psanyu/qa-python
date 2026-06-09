import mysql.connector

conn = mysql.connector.connect(option_files='C:/Users/pandi/QuerySurge/.my.cnf')

cursor = conn.cursor()
query = "SELECT * FROM imdb_movies LIMIT 100"
cursor.execute(query)
rows = cursor.fetchall();

for row in rows:
    print(row)

conn.close()