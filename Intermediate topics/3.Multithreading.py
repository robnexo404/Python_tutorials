from Terminal import clear_terminal
# Normally, python runs things in series(reads code top to bottom) but what if you need 2 or more things to run simultaneously?
#Threads do that. They run simultaneously and they can synchronise themselves, etc.
# lets start with importing the threading module:
import threading


def helloworld():
    print("Hello World")

t = threading.Thread(target= helloworld) #making the thread target the helloworld function 
t.start()  #running the thread


#Printing hello world isnt very interesting so lets make more complicated functions:

def function1():
    for x in range(10):
        print("ONE")
def function2():
    for x in range(10):
        print("TWO")
t1 = threading.Thread(target= function1) 
t2 = threading.Thread(target= function2) 

t1.start()
t2.start()
clear_terminal()
#without threading f2 would have to wait until f1 is finished
# threads made f1 and f2 print so fast, python had trouble deciding which one to print
# threading is very useful for games 

#to make a thread finish runing and then go onto the next code, type join
def Hello():
    for x in range(50):
        print("hello!")
t3 = threading.Thread(target= Hello)
t3.start()
t3.join()
print("I Should run last")
#without join, the text would be printed first
