length = int(input("Enter length:"))
breadth = int(input("Enter breadth:"))

for i in range(1, length+1):
    for j in range(1, breadth+1):
        if(i == 1 or i == length or
           j == 1 or j ==breadth ):
            print("*", end="" )
        else:
            print(" ", end="")

    print()
