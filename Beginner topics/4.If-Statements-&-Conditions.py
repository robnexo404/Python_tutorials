#when comparing 2 variables , we use a combination of these <, >, =, != and more. what if we want something to happen when x = y or x!=y ? 
#we use if statements, which are statements(a bit like a sentence that states or declares something) that return true or false. for example:
x = 5
y = 3
#for if statements, the double equals sign is used "=="
if x == y:
    #if...: do something . for example print"the nubmers are the same":
    print("The numbers are the same")
#the x==y statement alone returns true or false. we can show this by printing x==y:
print(x==y) #outputs false, the numbers arent the same.

#in other words:
if (x==y) == True:
    print("The numbers are the same")
#the "== True" part is just hidden.
#if statements are like "check" gates controlled and restricted by what you put in




#what if you want to "check" if the statements arent the same? you can use the ! = sign together meaning "not equal to":
if x!=y:
    print("numbers arent the same") 

#an else: means if all the other statements dont check anything, run whatever is under the else statement
if x==y:
    print("numbers are the same")
else:
    print("no if statement detected anything")




#now what about another statement, where the numbers arent the same?
#we can just add another if statement.
if x!=y:
    print("numbers arent the same")
#if we join them, we will have two if statements regarding the same thing so we change it to an elif(else + if) statement to make it look clearer:
if x==y:
    print("numbers are the same")
elif x!=y:
    print("numbers arent the same")

#so a proper statement would look like this:
if x==y:
    print("something")
elif x!=y:
    print("something")
else:
    print("something")

