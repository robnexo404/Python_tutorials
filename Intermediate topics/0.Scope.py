#a scope is where in the code something is.
#Anything inside a function is its "local" scope
#Anything outside is said to be in a "global" scope

#One thing to remember is that local variables cant be accessed from outside a function:
def Making_Var():
    x = 5
Making_Var()
#"print(x)" will cause an error
#A way around this is to create a global variable within the function:
def GlobalVar():
    global x  #creating a global variable called x
    x = 5
GlobalVar()
print(x) #will output 5

#if we have a function inside a function, we can use the word "nonlocal" to make the variable belong to the outer function:
def f1():
    x = "John" #making a local x 
    def f2(): 
        nonlocal x #using the x from the outer function
        x = "Hello" #changing x
    f2() # running the changed x function
    return x #giving back x for it to be printed
print(f1()) #prints "hello", because the inside function changed x to hello