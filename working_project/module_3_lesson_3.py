#create a students class
class students:
    
    def __init__(self, first, last,student = []):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@stutern.com'
# print('parent class created successfully')

#creating instance of the parent class
stud_1 = students('Bukola', 'Dare')
stud_2 = students('Temitope', 'Balogun')
# print(stud_1.first)

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
        '{} {}' .format(self.first, self.last)
        return '{} {}' .format(self.first, self.last)