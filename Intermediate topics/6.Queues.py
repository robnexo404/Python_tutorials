import queue
#when we have multiple threads running, you need a structured way to access the data. for example:
numbers = [10,20,30,40,50,60,70] #if t1 takes 10, t2 should take 20. how do we tell them to take the next free element? queues!:

q1 = queue.Queue()
# queue works as if it is creating a list and when some thread tries to access it, it gives it the first one, and removes 1 from the list
numbers = [10,20,30,40,50,60,70]
for number in numbers:
    q1.put(number) #putting numbers in q

print(q1.get()) #you get 10
print(q1.get()) #you get 20,next,...
#this is a first in, first out queue. If we want to reverse the order, we make a last in, first out queue:

q2 = queue.LifoQueue()  #Last in First out

numbers = [1,2,3,4,5,6,7]
for x in numbers:
    q2.put(x)
q2.get() #you get 7

#if you dont want either type of queue, you can use a priority queue
 
q3 = queue.PriorityQueue()

q3.put((2, "Hello World"))  #We now specify the priority of the element. The lower the number, the higher the priority
q3.put((11, 99))
q3.put((5, 7.5))
q3.put((1, True))
while not q3.empty():
    print(q3.get()[1])#you can do [1] to get the 2nd element