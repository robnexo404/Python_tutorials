from Terminal import clear_terminal
    


# As mentioned before, python is an object oriented programing language. Now lets use it:
# OOP allows you to make classes and objects for better organisation and reusability
# An easy way to understand objects and classes is with an example:
# A Car is the class and the object(s) is Volvo
# A Class  is like the main category and the objects are like the subcategories

# To make a class, we use the keyword "class":
class MyClass:
    x = 5
# To make an object, we can use the class MyClass:
p1 = MyClass()
print(p1.x) #prints 5
# You can delete an object using "del":
del p1

#we can create multiple objects from the same class:
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()
print(p1.x)
print(p2.x)
print(p3.x)
del p1, p2, p3
#classes cant be empty so if you need an empty class, you put the pass statement(Avoids getting an error):
class Empty():
    pass


clear_terminal()


# The __init__ method is used to assign values to object properties, or to perform necessary operations when the object is being created
# As we have seen earlier, classes can be thought of as the "blueprint" for an object. The __init__ stands for initialise, it runs when creating an object.
# Now, lets use it to assign values to the object:

class Person1:  # we can think of 'self' as the object id that we are putting in when creating the object. Here, we 
    def __init__(self, name: str, age: int) -> None: #Here, we can use the type annotations to make the code look cleaner
        self.name = name # we have to specify what happens when trying to acces p1.name or p1.age
        self.age = age

p1 = Person1("Bob", 35) #remember that we need to specify each variable

print(p1.name)
print(p1.age)
del p1
# We can set the default value for a var by typing age=18 for example


clear_terminal()


# We can now add an extra function inside :
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self): #For a function using self, you need to specify it inside the () brackets
        print(f"Hello, my name is {self.name}")

p1 = Person2("Bob", 35)
p1.greet()
del p1
# Note: Self can be renamed to anything you want


clear_terminal()


# Now what if we want the atributes of a person to be listed nicely when typing print(p1/p2/ect.) ? 
# We can use the __str__ to describe what happens when we force the p1,... to become a string(which we are doing with print(p1)):

class Person3:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height) #we can use .format too instead of f string 
        #it returns the name, age, height
    

p1 = Person3("Bob", 35, 180)
#now we can print p1:
print(p1)

del p1


clear_terminal()


# Say we want to have a population counter that would go up when a person is created and go down when a person is deleted
# This is how we access and edit variables in classes:
class Person4:
    population = 0

    def __init__(self, name: str = "Unknown", age: int = 18, height: int = 180) -> None: #sets default values for each var
        self.name = name
        self.age = age
        self.height = height
        #Now, we can access the 'population' wit Person4.population
        Person4.population += 1 #adding 1
    
    def __del__(self):
        Person4.population -= 1 #decreasing by 1
    
    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)

    def get_older(self, years): #an extra function for adding age
        self.age += years
        
p1 = Person4("Bob", 35, 180)
p1.get_older(10)
print(p1)


print(f"The current population is: {Person4.population}")

