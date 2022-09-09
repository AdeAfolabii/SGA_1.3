import sqlite3
#create a connection
conn = sqlite3.connect('items.db')
#create a cursor object
c = conn.cursor()
#check
print( 'All successful')

#creating a database table for Items sold in the store
# c.execute (
#    """
#    CREATE TABLE stationary (
#        item_id INTEGER,
#        name TEXT,
#        cost_price REAL,
#        quant_in_stock INTEGER
#       )
#     """
# )

#check
#print('table has been created successfully')

stationary_list= [
    ("123", "pencil", "1.50", "22"),
    ("321", "Extrpen", "7.50", "20"),
    ("214", "Eraser", "2.00", "10"),
    ("143", "Notebook", "3.00", "12"),
    ("412", "Ruler",    "1.50", "5"),
    ("124", "Crimp",    "0.50", "2"),
    ("121", "Tack",    "1.20", "33"),
    ("221",  "Glue",    "2.50", "1"),
    ("1234", "Hardnote", "8.50", "15"),
    ("4321", "Glitter", "6.50", "27"),
    ("3214", "Cord",    "4.50", "3"),
    ("3412", "Folder", "5.00", "23"),
    ("2135", "Paper",  "10.50", "156"),
    ("1254", "Ipad",  "30.70", "12"),
    ("0407", "Clip", "1.10", "37")
]

c.executemany( 
    """ 
    INSERT INTO stationary
    VALUES (?, ?, ?, ?) 
    """, 
    stationary_list 
)

query = """
 SELECT 
    item_id, name, cost_price, quant_in_stock
 FROM 
    stationary
 WHERE 
    quant_in_stock <= 10
ORDER BY 
    cost_price DESC
 """
 
c.execute(query)
items= c.fetchall()
print(f" item_id\t name\t cost price\tquant_in_stock")
print(f"{'-' * 100} ")

results=''.join(map(str, items))
print(results)
