#lets calculate the factorial of n
from Terminal import clear_terminal
#this is the non recursive way:
n = 7
fact = 1
while n >0:
    fact = fact * n
    n -=1
print(fact)

#this is the recursive way:
def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n-1)
        return number
print(factorial(7))
clear_terminal()

#fibonacci sequence function
def fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        a, b =b, a+b
    return a
print(fibonacci(3))
#recursive:
def fibonacci2(n):
    if n <=1:
        return n
    else:
        return (fibonacci2(n-1) + fibonacci2(n-2))
print(fibonacci2(3))
