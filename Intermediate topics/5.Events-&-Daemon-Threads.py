#Events are things that we can triger. First lets import threading:
import threading

event = threading.Event()

def myFunction():
    print("waiting for event to trigger")
    event.wait()                         #waits for the event
    print("Performing action xyz now...")
t1 = threading.Thread(target=myFunction)
t1.start() 

x = input("Do u want to trigger the event? (y/n)")
if x.upper() in("Y", "YES"):
    event.set()                     #triggers/sets the event 


#--------------
#DAEMON THREADS
#--------------
# Daemon threads run in the background regardless of the script "Nobody waits for daemon threads."
#they are very usefull for constantly reading a file for example
import time
path = "text.txt"
text = ""

#daemon thread function
def readFile():
    global path, text
    while True:
        with open("text.txt", "r") as f:
            text = f.read()
        time.sleep(3)

def printloop():
    for x in range(30):
        print(text)
        time.sleep(1)
t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printloop)
t1.start()
t2.start()
#so if t2 is done, the program is finished. no one waits for daemon threads. if t1 would be done, nothing would happen