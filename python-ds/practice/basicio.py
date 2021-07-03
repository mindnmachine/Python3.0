import sys

n= len(sys.argv)
args = sys.argv
print('No of command line args =',n)
print('The args are ',args)
print (' The args one by one')
for a in args:
    print(a)