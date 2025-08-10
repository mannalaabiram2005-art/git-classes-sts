# This is a module file

# Lets define some complex functions

# 1. Function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 2. Function to calculate the fibonacci of a number
# fibonacci is a series of numbers in which each number is the sum of the two preceding ones
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:   
        
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 3. Function to calculate the sum of first n natural numbers
# sum of first n natural numbers is the sum of all natural numbers from 1 to n
# sum of first n natural numbers = n * (n + 1) / 2
# ex sum of first 5 natural numbers = 5 * (5 + 1) / 2 = 15
def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n-1)


if _name_ == "_main_":
    print(factorial(5))
    print(fibonacci(5))
    print(sum_natural(5))
