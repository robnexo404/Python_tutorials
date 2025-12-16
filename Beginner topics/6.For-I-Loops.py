#While loops require extra outside variables to only repeat the loop a set amount of times. A better alternative would be using for i loops:
#making a list
x = [1, "a", 3.14]
#for i in x loops  work by doing that thing for every element of "x". this is very usefull and in this case the elements dont matter. only the amount of them does. The i can be replaced with anything.
for i in x :  #for every element in set x, do this:
    print("doing something (num of elements in x) times")
#we can also print i:
print(i)
#its 3.14 because as it looped throught every element in x, it reached the last one , 3.14
#Remember that the loop does the operation for every element in x.

# to make a loop repreat an x amount of times we can add a range(3) which will repeat 3 times
for i in range(3):
    print("doing it 3 times")
# range() acctually takes in a start, stop, step which we can use:
for i in range(1, 10):
    print("doing it 9 times") # it doesnt include the 10
for i in range(1, 10, 2):
    print("only counts every second number")
# the only value it absolutely needs is the original 3 or whatever number you want


#Its important to know that you can exit out of a loop with the 'break' word and continue with 'continue'