#program to find laragest of 3 nos
a1 = int(input("enter no:-"))
a2 = int(input("enter no:-"))
a3 = int(input("enter no:-"))
m = max(a1,a2,a3)

print(f"{m} is greatest no.")
#Write a program to find divisibilty
num=int(input("Type your number here:\n"))
num=int(input("Enter a number:"))
if num%2==0 or num%3==0 or num%7==0 or num%11==0:
    print("The number is divisible by either 2,3,7 or 11")

# Write a conversion program between cm and inches
b=int(input("Type your length in cm: \n"))
if b<0:
    print("Invalid number")
else:
    b=b/2.54
    print(b)

# Write a program to input a number and check if it is a perfect square
import math
b=int(input("Type your number to determine if it is a perfect square :"))

if(b <0):
    print(" Square root of a value less than 0 is imaginary")
elif((b-(math.sqrt(b))**2) == 0):
    print("{0:d} is a perfect square".format(b))
else:
   print("{0:d} is not a perfect squarex ".format(b))


# Income Tax
num=int(input("Type your salary "))
if num>=69000:
    num*=0.2
    print("Monthly salary is ",num)
elif  47500<=num<=68999:
    num*=0.15
    print("Monthly salary is ",num)
elif  num<=47999:
    num*=0.1
    print("Monthly salary is ",num)
else:
    print("Not high enough to be taxed!")

#WAP that accepts a character from the keyboard and determines whether it is a vowel or consonant or a number or a special symbol. Also find if it is upper case or lowercase if it is an alphabet.

