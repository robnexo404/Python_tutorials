from Terminal import clear_terminal
clear_terminal()
# Seq 1 to 9,000,000
def mygenerator(n):
    for x in range(n):
        yield x**3  #yield is like a return but it allows for more than one return and stores them 

values = mygenerator(10)
#to get the nth term:
print(next(values))
#we can get all the values of values with this:
for x in values:
    print(f"{x}")
#The cool thing about generators is that the value you put in doesnt change its memory/storage amount
clear_terminal()

def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5 

values = infinite_sequence()

for x in range(10):
    print(next(values))

#Generates powers of 5 without storing them individualy