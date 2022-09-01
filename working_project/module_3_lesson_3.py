#create a students class
class students:
    
    def __init__(self, first_name, last_name,student = []):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@stutern.com'
print('parent class created successfully')

#creating instance of the parent class
stud_1 = students('Bukola', 'Dare')
stud_2 = students('Temitope', 'Balogun')
print(stud_1.first_name)

#creating a child class
class group_leader(students):
    def __init__(self, first, last,student = []):
        super().__init__(first,last)
        self.student = student

# Define a method that adds students to the list of student under the group leader
def add_student(self, student):
        self.student.append(student)
        print(self.student, student)
print('student added successfully')

# Define a method that removes students from the list of students under the group leader
def remove(self, student):
        self.student.remove(student)
        print(self.student, student)
print('removed student successfuly')

# Define a method that prints out the full names of students in the list of students under group leader
def fullname(self):
        '{} {}' .format(self.first_name, self.last_name)
        return '{} {}' .format(self.first_name, self.last_name)

print('fullname successful')

#creating three more instances of the parent class
stud_3 = students("Chima", "Chukwu")
stud_4 = students("Joy", "Edet")
stud_5 = students("Seun", "Robert")
print(stud_4.first_name)

#creating two instances of the subclass 
G_lead_1 = group_leader("John", "Mark")
G_lead_2 = group_leader("Carlos", "Dre")

print(G_lead_2.last_name)

#Adding two students each to the list of students under the instance of the subclass
G_lead_1 = ["Mary", "chioma"]
G_lead_1 = ["Gideon", "uko"]
G_lead_2 = ["Amaka", "chukwu"]
G_lead_2 = ["Benita", "bamidele"]

#Removing the fullname of the student in the list of student under the instances of the subclass
G_lead_1 = ("Mary", "chioma")
G_lead_2 = ("Amaka", "chukwu")

#print the fullname of the student in the list of student under then instances of the subclass
print[G_lead_1.fullname()]
print[G_lead_2.fullname()]

#print the email of the instances of the subclass
def email(self, first_name, last_name):
        self.email = first_name + '.' + last_name + '@stutern.com'
print(G_lead_1.email)
print(G_lead_2.email)
    