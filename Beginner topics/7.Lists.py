#when making a list, you can access the elements of it with its index:
list = [1, 2, 3, 4, 5]
#an index is the number of each element in a list. Python makes the first element start with 0, so the second is 1, etc.
#we can access the index with [] brackets:
print(list[1]) #prints 2
#we can also acces the last, second last element with -1, -2 ,etc. 
print(list[-1]) #prints 5
#we can specify the range too and just like with range(), the first number is not counted:
print(list[0:3]) #prints [1,2,3]
#if you leave out the first number, it will outomaticaly start from the first
#if you leave out the last number, it will go till it reaches the end
#to find the length of the list we can use the len() operator:
print(len(list)) #outputs 5
#you can add, subtract elements with append(), remove(), etc. https://www.w3schools.com/python/python_lists_methods.asp 

