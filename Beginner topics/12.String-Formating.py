#to add a variable and string, you would usually use the + method. You can actually make it a lot easier with f strings(format(ed) strings):
var = "User"
fstring = f"Hello {var}" # we show that its a variable with {} brackets
print(fstring) #prints Hello User]
#if its a number, a modifier can be added after a colon:
price = 59
txt = f"The price is {price:.2f} dollars" #the .2f means a fixed, 2 decimal point number
print(txt)
#you can even put in the price directly:
price = 59
txt = f"The price is {59:.2f} dollars" 
print(txt)
#you can also do math operations within the {} brackets

#you can also use functions like .upper()
#for full f string capabilities, see https://www.w3schools.com/python/python_string_formatting.asp

#you can still manually format strings by adding a .format() but f strings are faster and the preferred way to format strings:
price = 49
txt = "The price is {} dollars"
print(txt.format(price)) 
#as you can see, the syntax is slightly different than normal


#its important to also know about '\n' :
#if i want to print on a new line after some function, string,etc I can put a '\n' :
name = "Bob"
string = f"Hello \n{name}"
print(string) # \n prints on a new line


