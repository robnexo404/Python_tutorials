#introduction to type annotations
#make sure your interpreter has type anotations on
#in python, to make our lives easier, we can denote the variable type when assigning it by adding ": (var type)":
intVar: int = 10
#you can still make it a string but your compiler should tell you that its the wrong type by underlining it:
intVar1: int = "hi"

#a second usefull usecase is when making functions:
def person(name: str, age: int) -> tuple: # the arrow tells the function what to return. In this case a tuple
    return (name, age)