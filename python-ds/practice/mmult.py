import sys
from numpy import *

r1,c1 = [int(a) for a in input("First Matrix rows, cols: ").split()]
r2,c2 = [int(a) for a in input("First Matrix rows, cols: ").split()]

if(c1 != r2):
    print("Matrix Multiplication not possible if Column 1 is not equal to Row 2", c1,r2)
    sys.exit()

str1 = input(' Enter First Matrix element:\n')

x = reshape(matrix(str1),(r1,c1))

str2 = input(' Enter Second Matrix element:\n')

y = reshape(matrix(str2),(r2,c2))

print(" The Matrix product is :", x*y)