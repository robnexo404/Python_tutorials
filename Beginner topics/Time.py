#when doing something like printing a 100 lines of strings, it can be so fast, you wont be able to read it untill it is done working. To solve this, we can add a delay:
#to add a delay, we need to import time:
import time
#to add a delay, we use time.sleep(time in seconds)
def Count(max: int):
    for i in range(1, max+1):
        time.sleep(1) #adds a delay between printing every number
        print(i)
max = int(input("What number do i count up to?"))
Count(max)