import sqlite3
print("imported successful!")

import csv

#connect to a database
conn = sqlite3.connect("2022_WAEC_Scores.db")
print("connect successful!")

#creating a cursor object
cursor = conn.cursor()
print("cursor connect successful!")

#creating a table
create_table = """
CREATE TABLE IF NOT EXISTS(

            ID INTEGER,
            Name TEXT,
            Maths INTEGER,
            English INTEGER,
            Physics INTEGER,
            Technical_drawing INTEGER,
            Further_maths INTEGER,
            Government INTEGER,
            Agriculture INTEGER,
            Geography INTEGER,
            Lit_in_english INTEGER
            )
            
            
        """




#check
print("table created successful!")

#load existing csv file
with open("WAEC_Scores.csv", "r") as opened_file:
    read_file = csv.reader(opened_file)
    
    cursor.executemany("""
    INSERT INTO  WAEC_Scores VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, read_file)

print("load csv file  successful!")

#querying he database
cursor.execute("SELECT * FROM WAEC_scores")
print("query successful!")

#format output to display in a tabular form
items =cursor.fetchall()

print("ID"+"\tNAME" + "\tMATHS" + "\tENGLISH" + "\tPHYSICS" + "\tTECHNICAL_DRAWING" + "\tFURTHER_MATHS" + "\tGOVERNMENT" + "\tAGRICULTURE"+"\tGEOGRAPHY" + "\tLIT_IN_ENGLISH" "\n" f"{'.' * 100}")

#looping through the items
for item in items:
     ID, Name, Maths, English, Physics, Technical_drawing, Further_maths, Government, Agriculture, Geography, Lit_in_english = item

#the student with highest score in maths
def highest_in_maths():
    cursor.execute("""
    SELECT Name, MAX(maths) FROM WAEC_scores
    """)
    item = cursor.fetchall()
    print(f"student with the highest score in maths, {item}")
highest_in_maths()

#The student with lowest score in english
def lowest_in_civic():
    cursor.execute("""
    SELECT Name, MIN(civic) FROM WAEC_scores
    """)
    item = cursor.fetchall()
    print(f"student with the lowest score in civic, {item}")
lowest_in_civic()

#The average score of students in maths
def average_in_maths():
    cursor.execute("""
    SELECT AVG(MATHS) FROM WAEC_scores
    """)
    item = cursor.fetchall()
    print(f"Average score of students in maths, {item}")
average_in_maths()

#the best performing student across all nine subjects in terms of overall scores
def best_performing_student_overall_scores():
    cursor.execute("""
    SELECT Name, MAX(best_students)
    FROM WAEC_scores
    SUM(Maths + civic + Physics + Technical_drawing + Further_maths, Government, Agriculture, Geography, Lit_in_english
    GROUP BY Name)
    """)
    item = cursor.fetchall()
    print(f"best performing student across all nine subjects in terms of overall scores, {items}")
best_performing_student_overall_scores()

#the best performing student across all nine subjects in term of average scores
def best_performing_student_average_scores():
    cursor.execute("""
    SELECT Name, MAX(best_students)
    FROM WAEC_scores
    AVG(Maths + civic + Physics + Technical_drawing + Further_maths, Government, Agriculture, Geography, Lit_in_english
    GROUP BY Name)
    """)
    item = cursor.fetchall()
    print(f"best performing student across all nine subjects in terms of overall scores, {items}")
best_performing_student_average_scores()

