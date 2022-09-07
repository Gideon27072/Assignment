import sqlite3

print("import successful!")

#connect to a database
conn = sqlite3.connect('sales.db')
print("connect successful!")

#creating a cursor object
cursor = conn.cursor()
print("cursor connect sucessful!")

#format output to display in a tabular form
items = cursor.fetchall()
print("item_ID"+ "\t\t\tname"+ "\t\t\t\tcost_price"+ "\t\t\t\tquantity_in_stock" "\n" f"{'.' * 90}")

#looping through the items
for item in items:
    item_ID, name, cost_price, quantity_in_stock = item
    print(f"{item_ID}\t\t\t{name}\t\t\t\t{cost_price}\t\t\t\t{quantity_in_stock}")

#calculating the amount the business owner invented in the procurement of the items
cursor.execute("SELECT SUM(cost_price) FROM inventory_data")
item = cursor.fetchall()
print("the amount invested by the business owner in the procurement of the items: ", item)

#calculating the average quantity of items in stock
cursor.execute("SELECT AVG(quantity_in_stock) FROM inventory_data")
item = cursor.fetchall()
print("the average quantity of items in stock: ", item)

#calculating the least quantity of items in stock
cursor.execute("SELECT name, MIN(quantity_in_stock) FROM inventory_data")
item = cursor.fetchall()
print("the least quantity of items in stock: ", item)

#calculating the item with the most quantity in stock
cursor.execute("SELECT name, MAX(quantity_in_stock) FROM inventory_data")
item = cursor.fetchall()
print("the item with the most quantity in stock: ", item)

# #commit the database and table
# conn.commit()

# #close the connection to the database
# conn.close()