#when a piece of code involves something that can result in an error if something goes wrong, you might want to use the try -> except method:
#a random function that lets user input a number:
def numb():
    int(input("Pick a number: "))
#Now, what if the user inputs a string instead? no problem, just force the input to be an int.
#NO! NO! NO! Now, if the input is used as a number elswhere, it will raise an error. 
#What we do instead is 'try' to run it. We also need to specify what happens when it cant use it:
def num():
    try:
        int(input("Pick a number: ")) #tries to run this
    except:                           #if it cant run the original, it runs this instead:
        print("Wrong type. Please enter an int") 
        num()                         #Runs the original function again untill input is correct type
num()
#You can also add an else: statement at the end to run if nothing goes wrong