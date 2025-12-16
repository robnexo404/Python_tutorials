# lets say 2 threads are changing the same thing/variable, that would be problematic. To fix this we synchronise threads

#------------
#LOCKING
#------------
#we will make 2 functions that will counteract each other, causing a problem
#locking will "lock" the resource/variable from threads
import threading
import time

x = 8192

lock = threading.Lock()

def double():
    global x, lock  #to change x
    lock.acquire()  #tries to get lock, waits if a thread already locked it
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(0.1) #waits a second to make it readable
    print("reached maximum")
    lock.release()
def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(0.1)
    print("reached minimum")
    lock.release()
t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)
 
#t1.start() #to run, uncomment it
#t2.start()

#----------
#SEMAPHORES
#----------
#these semaphores alow threads to access recources but they restrict it to a couple of accesses
# Lets define the semaphore:
semaphore = threading.BoundedSemaphore(value=5) #Only allows 5 accesses

def access(thread_number):   #assigning a number to each thread so we know which thread is trying to access or lock the resource
    print(f"{thread_number} is trying to access!")
    semaphore.acquire()
    print(f"{thread_number} was granted access!")
    time.sleep(10)                                   #waits 10 secs before releasing
    print(f"{thread_number}  is now releasing!")
    semaphore.release()

for thread_number in range(1,11):
    t = threading.Thread(target=access, args=(thread_number,)) # this is how to pass the parameter(s)
    t.start()
    time.sleep(1)