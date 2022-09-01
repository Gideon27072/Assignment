import sqlite3
print("imported successful!")

#connect to a database
conn = sqlite3.connect('sales.db')
print('connected successful!')

#create a cursor object
cursor = conn.cursor()
print("cursor connected successful!")

#creating a new table
cursor.execute("""create table inventory_data(
    item_ID integer primary key,
    name text,
    cost_price real,
    quantity_in_stock integer
    )
    
""")
print("table created successful!")

#inserting several values to the table
stationaries_list = [('1', 'marker', '30.0', '49'),
                     ('2', 'pen', '20.0', '45'),
                     ('3', 'ruler', '30.0', '27'),
                     ('4', 'stapler', '70.0', '35'),
                     ('5', 'drawing paper' '60.0', '45'),
                     ('6', 'paper tape', '40.0', '20'),
                     ('7', 'color pencil', '50.0', '50'),
                     ('8', 'mathset', '80.0', '60'),
                     ('9', 'crayons', '90.0', '70')
                     ('10', 'note book', '60.0', '39')

]

print('list created successful!')

cursor.executemany("insert into inventory_data values (?, ?, ?, ?)", stationaries_list)

#querying the database
cursor.execute("select * from inventory_data")
print("query successful!")

#format output to display in a tabular form
items = cursor.fetchall()
print("item_ID" + "\t\tname" + "\t\t\tcost_price" + "\t\t\tquantity_in_stock" "\n" f"{'.' * 80}")

#looping through the items
for item in items:
    item_ID, name, cost_price, quantity_in_stock = item
    print(f"{item_ID}\t\t{name}\t\t\t{cost_price}\t\t\t{quantity_in_stock}")

cursor.executr("""select * from inventory_data
WHERE quantity_in_stock < 2
ORDER BY cost_price DESC;
"""

)
item = cursor.fetchall()
print(item)