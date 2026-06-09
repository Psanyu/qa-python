import mysql.connector
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(
        option_files='C:/Users/pandi/QuerySurge/.my.cnf'
    )
    print('Connection Successful')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Check Credentials')
    else:
        print(err)

conn.close()