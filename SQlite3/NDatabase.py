#import sql
import sqlite3
#check
print('sqlite has been imported successfully')

#create a connection
conn = sqlite3.connect('SGAstudent.db')

#check
print('connection has been created successfully')

#create a cursor object
k = conn.cursor()

#check
print('cursor created successfully')

#creating a database table for Data science(ds) students
# k.execute (
#    """
#    CREATE TABLE SGA_1_3 (
#        first_name text,
#        last_name text,
#        email_address text,
#        course text
#       )

#     """
# )

# check
#print('table has been created successfully')

student_list= [   ("Abubakar","Adisa","adisaabubakar@gmail.com","Data science"),
    ("Ade", "Afolabi", "wasola.afolabi@yahoo.com","Data science"),
    ("Adedoyin","Abass","doyinabss0@gmail.com","Data science"),
    ("Amure","Faith","amuretalodabif@gmail.com","Data science"),
    ("Angela","Emmanuel","akhaneyelliemmanuel@gmail.com","Data science"),
    ("Tawa","Awonaike","purpleduralumin@gmail.com", "Data science"),
    ("Omowunmi","Awoniran", "mowunmi11@gmail.com", "Data science"),
    ("Binta", "Umar", "ubinta63@yahoo.com","Data science"),
    ("Bukola", "Ajayi", "bukolam.ajayi@gmail.com", "Data science"),
    ("Christian", "Uzondu", "uzonduchristian2@gmail.com", "Data science"),
    ("Cynthia", "Awiya", "awiyac@yahoo.com", "Data science"),
    ("Eniola", "Osadare", "dorcasosadare@gmail.com", "Data science"),
    ("Esther", "Akpanawo", "estherakpanawo@gmail.com", "Data science"),
    ("Ganiyat", "shittu", "ganiyatas@gmail.com", "Data science"),
    ("Idowu", "Adesanya", "idsworld22@yahoo.com", "Data science"),
    ("Iretioluwa", "olawuyi", "ireti.olawuyi@outlook.com", "Data science"),
    ("Jide","Adesugba", "Jide.Adesugba@yahoo.com", "Data science"),
    ("Joyce", "Ezeonwu",    "joyceokore@gmail.com", "Data science"),
    ("Temitope", "Bamidele", "bamideletemitope42@gmail.com","Data science")
]

# k.executemany(
#     """
#     INSERT INTO sga_1_3
#     VALUES (?, ?, ?, ?)
#     """,

# student_list
# )

print('successful')

# k.execute(
#     """
#     SELECT * FROM DS_1_3
#     """
# )

# print('Query successful')

# item = k.fetchall()
# print('FIRST NAME'+ '\t\tLAST NAME'+ '\t\tEMAIL'  +'\t\tCOURSE')
# print('----------'+ '\t\t---------'+  '\t\t--------'+'\t\t-----')


# for item in item:
#     print(item[0]  + "\t\t" + item[1] + "\t\t "+ item[2] +  "\t\t" + item[3])

# conn.commit()

#ALTERING TABLE
#CHANGING FROM SGA_1_3 TO DS_1_3

# k.execute("ALTER TABLE SGA_1_3 RENAME TO DS_1_3")

# # conn.commit()

# #check
# print("successful")

# #ADDING A NEW COLUMN

# # k.execute ("ALTER TABLE DS_1_3 ADD COLUMN SEX")
# # conn.commit()
# # print('successful')

#UPDATE STATEMENT
k.execute (""" UPDATE DS_1_3 SET sex = 'F/M' """)
conn.commit()

k.execute(""" SELECT * FROM DS_1_3 """)

items = k.fetchall()
print('FIRST NAME'+ '\t\tLAST NAME'+ '\t\tEMAIL'+   '\t\t\tCOURSE'+  '\t\tSEX')
print('---------------------------------------------------------------------------------------')

for item in items:
    print(item[0] + "\t\t" + item[1] +"\t\t"+ item[2] +"\t\t" +item[3] +"\t\t"+ item[4] )

conn.commit()

conn.close()
