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

c.execute(
   """
   INSERT INTO SGA_1_3
   VALUES ('Tomilayo', 'Afolabi', 'wahssy@gmail.com', 'data science')
   """
)

#INSERTING MULTIPLE RECORDS
record_list= [("Abubakar",  "adisa", "adisaabubakar@gmail.com", "Data science"),
    ("Adedoyin", "Abass", "doyinabss0@gmail.com", "Data science"),
    ("Amure",  "Faith", "amuretalodabif@gmail.com", "Data science"),
    ("Angela", "Emmanuel", "akhaneyelliemmanuel@gmail.com", "Data science"),
    ("Tawa",  "Awonaike", "purpleduralumin@gmail.com", "Data science"),
    ("Omowunmi", "Awoniran", "mowunmi11@gmail.com", "Data science"),
    ("Binta",  "Umar", "ubinta63@yahoo.com", "Data science"),
    ("Bukola", "Ajayi", "bukolam.ajayi@gmail.com", "Data science"),
    ("Christian",  "Uzondu", "uzonduchristian2@gmail.com", "Data science"),
    ("Cynthia", "Awiya", "awiyac@yahoo.com", "Data science"),
    ("Eniola",  "Osadare", "dorcasosadare@gmail.com", "Data science"),
    ("Temitope", "Bamidele", "bamideletemitope42@gmail.com", "Data science")
]

c.executemany(
    """
    INSERT INTO SGA_1_3
    VALUES (?, ?, ?, ?)
    """,

record_list

)

#print('Inserting multiple records at once')

c. execute(
    """
    SELECT * FROM SGA_1_3
    """
)

print('Query executed successfully')

items=c.fetchall()

# Displaying output in tabular form
print("first_name"+ "\t\t surname"+ "\t\t E-mail"+ "\t\t\t\t\t course \n" f"{'.' *100}")

#loop through items
for item in items:
    first_name, last_name, email, course =item
    print (f"{first_name:16}{last_name:16} {email}\t\t{course}")
