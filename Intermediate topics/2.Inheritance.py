#inheritence is when another class "inherits" traits from another
from Terminal import clear_terminal

class Person:
    population = 0

    def __init__(self, name: str = "Unknown", age: int = 18, height: int = 180) -> None: #sets default values for each var
        self.name = name
        self.age = age
        self.height = height
        #Now, we can access the 'population' wit Person4.population
        Person.population += 1 #adding 1
    
    def __del__(self):
        Person.population -= 1 #decreasing by 1
    
    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)

    def get_older(self, years): #an extra function for adding age
        self.age += years

# Lets Make a Worker:
#a worker is a person so we can state that inside ()
class Worker(Person):
    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)  #super is accessing the "parent" class
        self.salary = salary
    def __str__(self):                                  #overriding the __str__
        text = super(Worker, self).__str__()                    
        text += f", Salary {self.salary}"               #adding salary to the original 
        return text

    def calc_yearly_salary(self):
        return self.salary * 12

worker1 = Worker("Henry", 40, 176, 3000)
print(worker1)
print(worker1.calc_yearly_salary())

clear_terminal()


#Now, lets make our own function for adding and subtracting vectors
#this is called overloading
class Vector:

    def __init__(self, x: float , y: float):
        self.x = x
        self.y = y

    def __add__(self, other):  #making a function add
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"

v1 = Vector(2, 5)
v2 = Vector(6, 3)

print(v1)
print(v2)
v3 = v1+v2
print(v3)
