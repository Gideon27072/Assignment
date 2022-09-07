# import sqlite3
import sqlite3

print("import successful!")

# connect to a database
conn = sqlite3.connect('student_db')
print("connected successful!")

#create a cursor object
cursor = conn.cursor()
print("cursor connected successful!")

# #creating a new table
cursor.execute("""create table student_data(
               first text,
               last text,
               email text)
               
               
""") 
print("created successful!")

# #inserting several values to the table
# students_list = [('james', 'brown', 'jamesbrown@gmail.com'),
#                  ('john', 'carter', 'johncarter@gmail.com'),
#                  ('mary', 'prince', 'maryprince@gmail.com')
#                  ]
# print('student list created successfully!') 


#querying the database
cursor.execute("SELECT * FROM students_data")
print("query executed successful!")

#format output to display in  a tabular form
items = cursor.fetchall()
print("first" + "\t\tlast" + "\t\temail \n" f"{'.' * 60}")

#looping through the items
for item in items:
    first, last, Email = item
    print(f"{first:17}{last:16}{Email:28}")
    
conn.commit()
print("committed successful!")

#Alter table statement 
# change the table name

cursor.execute("Alter table students_data rename to group_info")
conn.commit()
print("Table renamed successful!")

#Adding a new column
cursor.execute("Alter table group_info ADD column Age")
print("New column added successful!")

#updating new column age with details
cursor.execute("update group_info SET age = '33'")
conn.commit()   
   
