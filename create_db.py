import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="college"
)

cursor=conn.cursor()
#create a database 
cursor.execute("CREATE DATABASE IF NOT EXISTS company_db")
cursor.execute("USE company_db")

#create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employee(
id INT AUTO_INCREMENT PRIMARY KEY,
name varchar(50),
salary INT
)
""")

print("Database and table created successfully")
conn.close()