from array import *

arr = array('i',[])
count  = 0
search = 0

print (' How many elements do you want to sort: ', end = '')
num = int(input())

for idx in range(num):
    print('Enter the :', idx+1, 'th value : ', end = ' ')
    arr.append(int(input()))

print('The original array is ', arr)

#Bubble Sort algorithm

for idx in range(num):
    for jdx in range(num-1-idx):
        if(arr[jdx] > arr[jdx+1]):
            temp  = arr[jdx]
            arr[jdx] = arr[jdx+1]
            arr[jdx+1] = temp
            count += 1

print(' Sorted Array is :', arr, ' number of iterations is :',count)
print(' Enter the number to be searched :')
search = int(input())
try:
    print(' Found the number at position :', arr.index(search))
except ValueError:
    print('The number was not found in :',search, arr)