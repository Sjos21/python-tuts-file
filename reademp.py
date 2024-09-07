import mysql.connector
conn=mysql.connector.connect(host='localhost',database='mydb',user='root',password='ShivuJoshi21')
if conn.is_connected():
    print("Connected to mysql db")

conn.close()