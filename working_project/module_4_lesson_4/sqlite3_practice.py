import sqlite3

#check
print("imported successfully")

# #connect to a database
# conn = sqlite3.connect('celebs.db')
# print("connected successful!")

# #create a cursor object
# cursor = conn.cursor()
# print("cursor connected successful!")

#creating a new table
# cursor.execute("""create table celebrity(
#                Name text,
#                Genre text,
#                Num_albums integer,
#                Age integer,
#                Awards integer,
#                Years_in_industry integer)
               
# """)

# print("Table created successful!")

# #inserting values to the table
# music_data_set = [('Davido', 'hiphop', '5', '28', '3', '12'),
#                   ('Wiskid', 'hiphop', '4', '32', '6', '14'),
#                   ('Burna boy', 'RnB', '6', '33', '7', '15'),
#                   ('Olamide' 'rock', '5', '34', '8', '13'),
#                   ('Tekno', 'hiphop', '3', '27', '8', '10'),
#                   ('Rema', 'RnB', '4', '21', '7', '10'),
#                   ('Fireboy', 'afro', '22', '3', '5', '10'),
#                   ('Joeboy', 'afro', '4', '24', '6', '9'),
#                   ('Crayon', 'rock', '3', '22', '0', '7'),
#                   ('Naira marley', 'hiphop', '6', '25', '1', '10'),
#                   ('juicewurld', 'RnB', '10', '20', '18', '15'),
#                   ('Ed sheeran', 'rock', '3', '26', '8', '3'),
#                   ('Bob marley', 'reggae' '14', '40', '12', '20'),
#                   ('Darmain marley', 'rock', '3', '36', '9', '15'),
#                   ('Tiwa savage', 'hiphop', '6', '35', '5', '13'),
#                   ('Dbanj', 'afro', '5', '39', '7', '12'),
#                   ('simi', 'soul', '4', '34', '7', '10'),
#                   ('Chris brown', 'RnB', '36', '7', '20', '16'),
#                   ('Lil wayne', 'rock', '38', '5', '8', '25'),
#                   ('Michael jackson', '40', 'soul', '6', '8', '30')
                  
#                   ]

# print("music_data set created successful!")

# cursor.executemany("insert into celebrity values (?, ?, ?, ?, ?, ?)", music_data_set)

# #querying the database
# cursor.execute("select * from celebrity")
# print("query executed successful!")

# #format output to display in a tabular form
# items = cursor.fetchall()
# print("Name" + "\t\tGenre" + "\t\tNum_albums" + "\t\tAge" + "\t\tAwards" + "\t\tYears_in_industry")
# print(items)

# #loop through the items
# for item in items:
#     Name, Genre, Num_album, Age, Awards, Years_in_industry = item
    
#     print(f"{Name:23}{Genre:13}{Num_album:12}{Age:12}{Awards:13}{Years_in_industry:14}")
    
# conn.commit()
# print("committed successful!")

# #the most decorated celebrity
# cursor.execute("""
# select name,MAX(Awards)
# from celebrity

# """)
# item = cursor.fetchall()
# print(item)

# #The oldest celebrity
# cursor.execute("""
# select name,MAX(Age)
# from celebrity

# """)
# item = cursor.fetchall()
# print(item)

# #The celebrity that has been in the industry the longest
# cursor.execute("""
# select name,MAX(Years_in_industry)
# from celebrity

# """)
# item = cursor.fetchall()
# print(item)

# #The celebrity with the least number of albums
# cursor.execute("""
# select name,MIN(Num_albums)
# from celebrity

# """)
# item = cursor.fetchall()
# print(item)

# #The most popular genre of music amongst all celebrities in the dataset
# cursor.execute("""
# select name,MAX(Genre)
# from celebrity

# """)
# item = cursor.fetchall()
# print(item)

# #commit th database and table
# conn.commit()

# #close the connection to the database
# conn.close()
