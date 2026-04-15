import mysql.connector as mydb
con=mydb.connect(user='root',
             password='root',
             host='localhost',
             database='STUDENTSDB')
cur=con.cursor()
# DATABASE
print('Connection is Done')
datasql='CREATE DATABASE STUDENTSDB'
cur.execute(datasql)
print('Database is CREATED')

#CREATING TABLE
tabque='CREATE TABLE students (sid int,name varchar(20))'
cur.execute(tabque)
print('Table is Created')

#INSERTING DATA
insqur='INSERT INTO students (sid,name) VALUES(%s,%s)'
value=[(2,'Raju'),(3,'Indumati'),(4,'Kaalia'),(5,'Jaggu'),(6,'Dholu')]
cur.executemany(insqur,value)
con.commit()
print('Data is Inserted')

#SELECT QUERIES
squr='SELECT * FROM students'
cur.execute(squr)
for i in cur:
    print(i)


cur.close()
con.close()