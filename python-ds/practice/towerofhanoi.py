import sys

def towers(num,src,dest, aux):
    
    if num == 1:
        print('Move disk 1 from pole %s to pole %s' %(src,dest))
        return
    towers(num-1, src,aux,dest)
    print ('Move disk %i from pole %s to pole %s'%(num,src,dest))
    towers(num-1, aux,dest,src)        
        


num = int(input('Enter the number of disks: '))
if (num > 0 and num <5):

    towers(num, 'A', 'C', 'B')