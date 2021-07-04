import sys
from numpy import *

def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    return result


print("Enter the number that you want to compute factorial of ",end = ' ')
num = int(input())

if (num > 0 and num <15):
    for idx in range(num + 1):
        print ('Factorial of {} is {}'. format(idx,factorial(idx)))
else:
    print("Invalid input you have exceeded the range")