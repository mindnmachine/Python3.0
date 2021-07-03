# Function to accept number of lines and print a pattern
def pattern(n):

    # outer loop through number of rows: n
    for i in range(0, n):
        # Set the value at the start of each loop
        value = 1
        # inner loop to handle number of columns 0 to i+1
        for j in range(0, i+1):
            # printing first and the last number except when i == n-1 
            if(value == 1 or value == i+1):
                print(value, end=" ")
            else:
                #printing pattern when i == n-1
                if(i == n-1):
                    print(value, end=" ")
                else:
                    #printing blank otherwise
                    print(" ", end=" ")
            value += 1
        print('\r')
      
# Calling Code
# Accept the number of lines you want to print in 1,2... formatn
num = int(input("Enter the number of lines you want to print : "))

# define a function to print the pattern
pattern(num)
