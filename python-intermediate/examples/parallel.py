rows = int(input("Enter rows:"))
cols = int(input("Enter Cols:"))

for i in range(0, rows):
    for j in range(1, i+1):
        print(" ", end="")
    for j in range(0, cols):
        print("*", end="")
    print()

