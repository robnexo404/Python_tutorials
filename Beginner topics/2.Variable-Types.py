#in python, you can create a variable and assign it a value:
variable = "something"
#this variable can be different data types: 
#int(intiger):
intiger = 10
#float(numbers with decimal points):
float = 3.14
#boolean(True or false):
boolean = True
#strings(text) | make sure to put in quotes:
string = "Hello World"
#lists(sequence of objects):
list = [10, "Hello", 3.14]
#dictionaries(a:b, c:d, ...):
dictionary = {"car":"BMW", "color":"black"}
#tuples(an ordered sequence of objects that cant be changed):
tuple = (10, "Hello", 3.14)
#sets(collection of unique objects):
set = {"a", "b", "c"}

#if you ever want to check the type, you can use the type() operator:
print(type(variable)) #Outputs str (short for string)

#You can also force a variable to become a data type:
forcedString = str(3.14)
print(forcedString)
#now if we check the type:
print(type(forcedString)) #Outputs str


