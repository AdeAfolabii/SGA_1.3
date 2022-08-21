#import sql
import sqlite3

#check
print('sqlite has been imported successfully')

#create a connection
conn = sqlite3.connect('dsstudent.db')

#check
print('connection has been created successfully'); print(type(conn))

#create a cursor object
c = conn.cursor()

#check
print('cursor created successfully \n', type(conn))


#creating a database table for Data science(ds) students
c.execute (
   """
   CREATE TABLE SGA_1_3 (
       first_name text,
       last_name text,
       email_address text,
       course text
      )

    """
)
# check
print('table has been created successfully')

