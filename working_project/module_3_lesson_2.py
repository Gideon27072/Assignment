#create a car class
class car:
    def __init__(self,color,name,model,engine,tyre):
        self.color = color
        self.name = name
        self.model = model
        self.engine = engine
        self.tyre = tyre
    
# calling the method a car
    def speed(self):
        print('The car moves at 120km/h')
    def capacity(self):
        print('it has a big fuel tank')
    def price(self):
        print('it will be sold at a high price')
    def height(self):
        print('it will be 670 inches')
    def type(self):
        print('it is a gasoline car')
    
#check if the class work
properties = car('red','toyota','c56','ecoboost','camaro')
print(properties.color)
print(properties.name)
print(properties.model)
print(properties.engine)
print(properties.tyre)