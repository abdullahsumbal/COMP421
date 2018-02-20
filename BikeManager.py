import psycopg2
import csv

# Connection to the database
db = psycopg2.connect(host="comp421.cs.mcgill.ca",database="cs421", user="cs421g29", password="XXX")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("INSERT INTO bikemanagers (bmemail , bmname , bmpassword) VALUES (%s,%s,%s);", ('muhammad1.sumbal@mail.mcgill.ca', 'Sumbal', 'yolo'))

# Fetch a single row using fetchone() method.
#data = cursor.fetchone()
#print ("Database version : %s " % data)
db.commit()

# disconnect from server
db.close()