#In python if you have a task that you want to do, for example print("hello, this is random text")
#If you want to copy it, you could do it manually(copy, paste line) or you can use functions:

#functions have to be built or 'defined' and given a name:
#def is short for define
def Function(): # in order for python to distinguish between something inside and outside a function, we indent('tab') the text:
    print("hello, this is random text")
#the function does not run untill we call it by stating the name with () brackets anywhere in the code:
Function() #hello, this is... will be printed 
#now we can easily call it anywhere we want it to run

#a function can also 'return' something.Returning stops the function and gives back what you put after the "return" word  By default it is None because we dont want anything back.
# Lets make a function return a string:
def strFunc():
    return "Random string"
#now, when we call it, it is like assigning the string to a variable:
strVar = strFunc()
#now we can print strVar
print(strVar) 
#OR
print(strFunc())

#If you leave a function empty, it will show as an error. Functions cant be empty, However we can use the word 'pass' to make it do nothing:
def PassFunc():
    pass 

# ARGUMENTS:

#Functions can also take in arguments that you can reference inside the function:
def Name(name):
    print(name+" is my name.")
#now when calling the function we give it a variable(an argument):
Name("Bob") 

#functions can take in as many arguments as you want(seperated by , ) but when calling the function, you have to give the amount of arguments it requires.
#you can however make the argument have a default value:
def Name2(name = "bob"):
    print("my name is ", name) #we can also use a comma instead of a plus 
#now we are allowed to not provide an argument:
Name2()#prints my name is bob
#you can also manualy pick the what the argument is equal to:
Name2(name="Dave")#prints my name is Dave


#an example of great use of the loops we have learned about:
def my_function1(fruits):
  for fruit in fruits: #for every element in the given fruits, do this:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"] #creating a list of items for the function
my_function1(my_fruits)

#we can still 'return' variables



# EXTRA ARGUMENTS:

#if you dont know the amount of each variable you will need, you can put a * before the variable:
def my_function2(*kids): #an unknown amount of "kids"
  print("The youngest child is " + kids[2]) #telling which "kids" to use

my_function2("Emil", "Tobias", "Linus") #prints Linus
# a double ** before an argument means you dont know how many variables will be added
def my_function(**kid):
  print("His last name is " + kid["lname"]) #stating which argument to use

my_function(fname = "Tobias", lname = "Refsnes")

#you can also "unpack" lists with "*" and dictionaries with "**"
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)