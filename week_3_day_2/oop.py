# #classes in python
# class Mycounter:
    
#     def set_count(self, n):
#         self.count = n
        
#         print(self.count)

# #create an object of the class
# counter_object = Mycounter()

# #call a method of the class
# counter_object.set_count(5)

# counter_object_2 = Mycounter()

# counter_object_2.set_count(7)

class Animal:
    
    def eat(self):
        
        print("i am eating")
    
    def poop(self, what_i_ate):
        
        self.what_i_pooped = what_i_ate
        
        print(self.what_i_pooped)
    
    def sleep(self, how_i_long_sleep):
        
        self.i_sleep_for = how_i_long_sleep
        
        print(self.i_sleep_for)
        
# create the first instance of the Animal class
# dog = Animal()
    
# dog.eat()

# dog.poop('bone') 

# dog.sleep(7)

# human = Animal()

# print(type(dog))

# class Employee:
    
#     def __init__(self, name, id, department, salary=300000):
#         self.salary = salary
#         self.name = name
#         self.id = id
#         self.department = department
    
#     def give_raise(self, raise_value):
#         self.salary = self.salary + raise_value
#         print(self.salary)
#         return self.salary
    
# #first employee
# first_employee = Employee(name='Gideon', id=1, department='Data Science')

# print(first_employee.name)
# print('salary before raise: ', first_employee.salary)
# print(first_employee.department)

# first_employee.give_raise(250000)

# print('salary after raise: ', first_employee.salary)

