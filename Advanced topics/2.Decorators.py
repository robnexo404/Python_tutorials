# decorators add or "wrap" another functionality around a function, changing its behaviour without changing the original 
from Terminal import clear_terminal
clear_terminal()

def mydecorator1(function):  #decorator takes in function:
    def wrapper():          #wrapper adds something to the function, eg, print()
        print("I am decorating your function!")
        function()          #calls original function to still have a part of its original functionality

    return wrapper          #gives back the wrapper to be able to call it and apply the change


def hello_world_demo():
    print("helloworld")

mydecorator1(hello_world_demo)() # takes in the helloworld function and calls the wrapper function 
clear_terminal()

#That is the main idea behind a decorator in python but its done differently:
#instead of calling the decorator and then the wrapper, we do this:
#we add a @decorator before defining the function:
@mydecorator1
def hello_world():
    print("Hello World!")
#Now all we need to do is simply call the function:
hello_world()
clear_terminal()

#this is fine but what if we are passing an argument?
@mydecorator1
def hello1(person):
    print(f"Hello {person}")
#hello1("Mike") results in an error because the wrapper doesnt take in arguments
#lets make it "universal" and take in any arguments we want. We do this with:
# *args(if there is an unknown amount of arguments)
# **kwargs(if there is an unknown amount of keyword arguments (name=""))

def mydecorator2(function):
    def wrapper(*args, **kwargs):
        print("I am decorating your function")
        function(*args, **kwargs)
    return wrapper
@mydecorator2
def hello2(person):
    print(f"Hello {person}!")

hello2("Mike") #Now works

clear_terminal()
#this is fine but it doesnt work if i want to return something. I could add a return in the wrapper, but the order of it returning and printing would be messed up.
#the best way to do this is like this:
def mydecorator3(function):
    def wrapper(*args, **kwargs):
        print("I am decorating your function")
        return_value = function(*args, **kwargs)
        return return_value
    return wrapper
@mydecorator3
def hello3(person):
    print(f"Hello {person}!")
    return f"Hello {person}!"

print(hello3("Mike")) #Now works comepletely fine
clear_terminal()


#Practical Example #1 - Logging

def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
        return value
    return wrapper
@logged
def add(x, y):
    return x+y
print(add(10, 20))

clear_terminal()

#Practical Example #2 - Timing
import time 

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} seconds to execute!")
        return value
    return wrapper
@timed
def myfunction(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result
a = myfunction(1000)
