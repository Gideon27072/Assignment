import sqlite3

#connect to a database
conn = sqlite3.connect("SGA_1_3_learners.db")

#create a cursor that allows sql statemen to be executed
cursor = conn.cursor()



#create a cursor
cursor = conn.cursor()

#create a table called learners into the database SGA_1_3_learners 
learners_list = [("Praise", "Emmanuel", "praiseemmanuel@gmail.com", "Data Science"),
                 ("Prince", "Ekeocha", "princeekeocha@gmail.com", "Data science"),
                 ("Rasheedat", "Sikiru", "rasheedatsikiru@gmail.com", "Data science"),
                 ("Ramotllah", "Jubril", "ramotallahjubril@gmail.com", "Data science"),
                 ("Sheriff", "Azeez", "sheriffazeez@gmail.com", "Data science"),
                 ("Temitope", "Bamidele", "temitopebamidele@gmail.com", "Data science"),
                 ("Theresa", "Karamor", "theresakaramor@gmail.com", "Data scince"),
                 ("Tina", "Uyateide", "tinauyateide@gmail.com", "Data scinence"),
                 ("Victoria", "Chukwuno", "victoriachukwuno@gmail.com", "Data science"),
                 ("Deborah", "Olorunnishola", "deboraholorunnishola@gmail.com", "Data science"),
                 ("Cynthia", "Awiya", "cynthiaawiya@gmail.com", "Data science"),
                 ("Christian", "Uzondu", "christianuzondu@gmail.com", "Data science"),
                 ("Binta", "Umar", "bintaumar@gmail.com", "Data science"),
                 ("Bukola", "Ajayi", "bukolaajayi@gmail.com", "Data science"),
                 ("Bamideji", "Adesugba", "bamidejiadesugba@gmail.com", "Data science"),
                 ("Awonaike", "Tawakalitu", "awonaiketawakalitu@gmail.com", "Data science"),
                 ("Adedoyin", "Abass", "adedoyinabass@gmail.com", "Data science"),
                 ("Adebisi", "Afolabi", "adebisiafolabi@gmail.com", "Data science"),
                 ("Abubakar", "Adisa", "abubakaradisa@gmail.com", "Data science"),
                 ("Eke", "Ihuoma", "ekeihuoma@gmail.com", "Data science"),
                 ("Esther", "Akpanowo", "estherakpanowo@gmail.com", "Data science"),
                 ("Eniola", "Osadare", "eniolaosadare@gmail.com", "Data science"),
                 ("Etareimi", "louis", "etareimilouis@gmail.com", "Data science"),
                 ("Faith", "Amure", "faithamure@gmail.com", "Data science"),
                 ("Ganiyat", "Shittu", "ganiyatshittu@gmail.com", "Data science"),
                 ("Gideon", "Uko", "gideonuko@gmail.com", "Data science"),
                 ("Idowu" "Adesanya", "idowuadesanya@gmail.com", "Data science"),
                 ("Joyce", "Ezeonwu", "joyceezeonwu@gmail.com", "Data science"),
                 ("Kehinde", "Orolade", "kehindeorolade@gmail.com", "Data science"),
                 ("Placidus", "Ali", "placidusali@gmail.com", "Data science"),
                 ("Omowunmi", "Awonirana", "omowunmiawonirana@gmail.com", "Data science"),
                 ("Ogechi", "Njemanze", "ogechinjemanze@gmail.com", "Data science"),
                 ("Mariam", "Adeoti", "mariamadeoti@gmail.com", "Data science"),
                 ("Lawrence", "Aneshimokha", "lawrenceaneshimokha@gmail.com", "Data science"),
                 ("Kafayat", "Ibrahim", "kafayatibrahim@gmail.com", "Data science")
                 ]

#inserting multiple rows into the learners table
cursor.executemany(
    """INSERT INTO learners
    VALUES(?, ?, ?, ?)""",
    learners_list
    
    )

print("insert succesful") 

#querying the learners table
cursor.execute('SELECT * FROM learners')

#check
print("Query executed!")

items = cursor.fetchall()
print(items)

# format output to display in a tabular form
print("first_name" +  "\tlast_name" "\temail" "\t\t\t\t\tcourse \n" f"{'.' * 90}")

# loop through the class
for item in items:
    first_name, last_name, email, course = item
    print(f"{first_name:17}{last_name:18}{email:31}\t\t{course}")