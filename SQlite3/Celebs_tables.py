import sqlite3
#check
print('successful')

#create a connection
conn = sqlite3.connect('celebs.db')

#check
print('successful')

#create a cursor object
c = conn.cursor()
#check
print('successful')

#creating a table for Celebrities
c.execute (
     """
     CREATE TABLE celebs (
       name TEXT,
       genre TEXT,
       age INTEGER,
       num_album INTEGER,
       num_awards INTEGER,
       years_in_industry INTEGER
      )

      """
)

#check
print('creation successful')

# #check
# print('successful')
