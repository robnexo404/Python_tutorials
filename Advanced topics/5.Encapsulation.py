from Terminal import clear_terminal
class Person:

    def __init__(self, name, age, gender):
        #the double underscores before the name makes it harder to access and can be thought of as "private"
        #this means we cant access it directly from outside the class.
        #FYI, its called name-mangling
        self.__name = name
        self.__age = age
        self.__gender = gender
        #We can make a property to access the name, age, etc
        #This allows for constraints when modifying the variables
        #just making the function name would be enough but to make it a property we add @property
    @property
    def name(self):
        return self.__name
    
    #name setter is used, because in python, you cant overload or overwrite a function without it
    #the setter lets us control/constrict the access to the variable 
    @name.setter
    def name(self, value):
        #Now, a constraint could be that when someone tryes to assign the name "Bob" to __name, it will be changed to "Default Name"
        if value == "Bob":
            self.__name = "Default Name"
        else:
            self.__name = value
    #@staticmethod allows us to not use the "self" word
    @staticmethod
    def mymethod():
        print("Hello World")
#Now we can call mymethod without the object because of the @staticmethod (it doesnt take in self):
Person.mymethod()

p1 = Person("Mike", 20, "m")
print(p1.name)

p1.name = "Bob"
print(p1.name)

clear_terminal()
#The creator said that @staticmethod was somewhat of a mistake. It comepletely removes the point of the object in the first place.
#a better way of doing it is to use @classmethod. This means instead of passing the self, we pass the cls(class) itself:
class Bot:
    def __init__(self, name):
        self.name = name

    @classmethod
    def Print(cls, message): #just like __init__ arguments but instead of self -> cls
        cls.message = message
        print(message)

#Now, we can give a message without having an object:
Bot.Print("Hello Humans")
