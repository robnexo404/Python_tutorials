#The cool thing about python is you can easily open and edit files:
#To open a file, you can use the open() operation, but you also have to specify what way are you opening the file:
#"r" to read only, error if file isnt there
#"a" to append(add to a file), or create file if not there
#"w" to write only, creates file if not there
#"x" to create file, error if file already exists

#lets open this file:
f = open("11.File-Handling.py", "r") #opens this file to read it only
#the file however, is not closed automatically. to do that, we use the 'with' word:
with open("11.File-Handling.py", "r") as f: #it also lets us refer it as a shortcut: f in this case
    print(f.readline()) #reads the first line of this file and automaticaly closes it. we can still close the file with f.close() :
f.close() 
#By default the read() method returns the whole text, but you can also specify how many characters you want to return:
with open("11.File-Handling.py", "r") as f:
    print(f.read(5)) #returns first 5 characters

#Now lets make a file and add something to it(we will use the write() function because append() only works if youre adding to something. In this case, theres nothing to add to):

#open("demo-text.txt", "x")    we can skip this because the "w" on the next line creates the file if none found
with open("demo-text.txt", "w") as f:
    f.write("Hello World")
with open("demo-text.txt", "r") as f:
    print(f.read())

#to delete a file, you have to import os and use the os.remove() function:
import os 
os.remove("demo-text.txt")

# a  better way of doing this is to check if it exists:
if os.path.exists("demofile.txt"): #checks if file exists
  os.remove("demofile.txt")
else:
  print("The file does not exist")