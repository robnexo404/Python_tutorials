#If you ever want to make a counter or a repetetive task, you can use a loop:
x = 3
y = 5
while x==y:
    print("doing this until the statement is false")
    #since the statement is false already, the loop will never run

# if we make x==y, the loop will never stop. how do we fix that?
# we can increase x until it becomes y, so that if we make a x!=y statement, the loop will run until x==y
#how do we increase x? we can just do x = x+1:

while x!=y:
    print("doing something until x==y ")
    x = x+1

#this is correct, but if we have a statement not involving the x we are raising:
a = 3
b = 5
while a==b:
    print("doing something until x==y")
    x = x+1
#the x will not affect the loop, so it would keep going forever if i set a!=b
#you have to be carefull with what variables youre using 

# x = x+1 is long so in python you can just write x+=1