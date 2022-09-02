import sqlite3
#create a connection
conn = sqlite3.connect('celebs.db')
#create a cursor object
c = conn.cursor()

Celeb_list = [ 
    ("Ariana Grande", "pop", "29", "9", "8", "14"),
    ("Ajax kirk",    "Rock", "35", "22", "55", "1.5"),
    ("Jon Bellion",   "Blues", "35", "5", "15", "10"),
    ("levi Ackerman",   "pop", "35", "3", "5", "2"),
    ("eren yaeger",    "blues", "18", "6", "8", "1"),
    ("Mikasa Ackerman", "rnb", "33", "9", "2", "4"),
    ("Beyonce Knowles", "funk", "29", "4", "8", "18"),
    ("Adriana Bailey",  "pop", "29", "9", "20", "4"),
    ("Meredith Grey",   "blues", "89", "7", "8", "14"),
    ("Christina Yang",   "metal", "29", "9", "0", "12"),
    ("Isobel Stevens",   "rock", "19", "5", "21", "13"),
    ("Arthur Pendragon",  "pop", "20", "3", "4", "1"),
    ("Meliodas Love",     "pop", "100", "5", "5", "3"),
    ("Elizabeth Liones",  "pop", "29", "6", "3", "6"),
    ("Inosuke Hashibira", "pop", "19", "7", "2", "7"),
    ("Tanjiro Kamado",    "pop", "19", "9", "1", "8"),
    ("Zenitsu Agamastu",   "pop", "19", "8", "28", "7"),
    ("Nezuko Kamado",    "Anime", "15", "9", "2", "2"),
    ("Tomioka Giyuu",    "Anime", "33", "9", "308", "5"),
    ("Naruto Uzumaki",  "Anime", "29", "9", "150", "3"),
    ("Sasuke Uchiha",   "Metal", "29", "9", "28", "5"),
    ("sakura haruno",   "funk", "29", "1", "35", "6"),
    ("Hinata Hyuga",       "pop", "29", "9", "2", "14"),
    ("Neji Hyuga",      "Blues", "29", "5", "208", "1"),
    ("Kakashi Hatake",   "Blue", "29", "2", "28", "5"),
    ("Ero sennin",       "pop", "99", "9", "508", "30"),
    ("Itadori yuuji",    "pop", "19", "9", "108", "7"),
    ("Megumi fushiguro", "metal", "29", "9", "28", "14"),
    ("Satoru gojo",   "Metal pop", "29", "9", "8", "14"),
    ("Nobara Kugisaki", "pop",  "29", "9", "28", "10"),
    ("Billie Eilish",    "pop", "20", "9", "100", "5"),
    ("green apple",     "pop", "29", "8", "7", "5"),
    ("Mike Posner",     "Funk", "29", "7", "2", "14"),
    ("James Arthur",     "blues", "29", "8", "1", "5"),
    ("Tears for fear",   "pop", "29", "6", "8", "28"),
    ("Charlie puth",     "RNB", "29", "7", "5", "8"),
    ("Post Malone",      "RNB", "29", "5", "1", "14"),
    ("Imagine Dragons",   "pop", "29", "8", "6", "19"),
    ("Zara Larsson",     "pop", "29", "9", "0", "14"),
    ("The Script",     "pop", "29", "9", "3", "14"),
    ("Major Lazer",    "dancehall", "29", "9", "88", "15"),
    ("Maneskin",       "pop", "29", "9", "28", "2")
    
]

c.executemany(
    """
    INSERT INTO celebs
    VALUES (?, ?, ?, ?, ?, ?)
    """,
Celeb_list
)

# def select_single_column (n=10, column='name', output_column_name= 'celeb_names'):
#     query = f"""
#     SELECT {column}
#     FROM celebs
#     """
#     c.execute(query)

#     items = c.fetchmany(n)
#     print(f"{output_column_name}\n{'_' *100} ")
    
#     for item in items:
#         print('' .join(item))

# select_single_column (n=10, column='genre', output_column_name= 'celeb_genre')

# SELECTING DISTINCT VALUES
# most decorated celebrity
query = """
 SELECT 
    name, genre, age, num_awards
 FROM 
    celebs
 WHERE 
    num_awards = (SELECT MAX(num_awards) FROM celebs)
 """
 
c.execute(query)

items = c.fetchall()
print(f" name \t\t genre \t\t age \t\t no_of_awards")
print(f"{'-' * 100} ")

results= ''.join(str(tup) for tup in items)
for item in items:
    print(results)

# OLDEST CELEBRITY
query = """
 SELECT 
    name, genre, age, num_awards
 FROM 
    celebs
 WHERE 
    age = (SELECT MAX(age) FROM celebs)
 """
 
c.execute(query)
   
items = c.fetchall()
print(f" name \t\t genre \t\t age \t\t no_of_awards")
print(f"{'-' * 100} ")

results= ''.join(str(tup) for tup in items)
for item in items:
    print(results)


#celebrity that has been in the industry the longest?
query = """
 SELECT 
    name, genre, age, num_awards, years_in_industry
 FROM 
    celebs
 WHERE 
    years_in_industry = (SELECT MAX(years_in_industry) FROM celebs)
 """
 
c.execute(query)

    
items = c.fetchall()
print(f" name \t\t genre \t age\t no_of_awards \t\t years in industry")
print(f"{'-' * 100} ")

results= ''.join(str(tup) for tup in items)
for item in items:
    print(results)

# celebrity has the least number of albums
query = """
 SELECT 
    name, genre, age, num_awards, num_album, years_in_industry
 FROM 
    celebs
 WHERE 
    num_album = (SELECT MIN(num_album) FROM celebs)
 """
 
c.execute(query)

items = c.fetchall()
print(f" name \t\t genre \tage\tno_of_awards\tno of albums\t years in industry")
print(f"{'-' * 100} ")

results= ''.join(str(tup) for tup in items)
for item in items:
    print(results)

# most popular genre of music among all celebrities
query ="""
SELECT genre,
       count(1)
FROM celebs
       GROUP BY genre
    HAVING count(1) > 5 
       ORDER BY genre DESC
"""
c.execute(query)
items = c.fetchall()
print(f"genre")
print(f"{'-' * 20} ")
for item in items:
    print(''.join(str(tup) for tup in items))

conn.commit()
conn.close()

