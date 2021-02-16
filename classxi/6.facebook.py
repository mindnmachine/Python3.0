
n = int(input("Enter the number of users to be be entered: "))
print(n)
cnt_dict = dict()
average = 0
mobile = 0
for i in range(n):
   a = int(input("Mobile Facebook User (0/1): "))
   x = input("Starting year of usage: ")
   y = int(input("Total number of minutes spent on FB per month: "))
   z = int(input("Time spent on FB per visit: "))
   
   print(n)
   cnt_dict[i] = a,x,y, z

print("Details of your users are: ")
print("id", "\t\t", "Starting year of usage", "\t", "Mins per month", "\t", "Time spent on FB per visit")
for i in cnt_dict:
   print(i, "\t\t\t", cnt_dict[i][1], "\t\t\t", cnt_dict[i][2],"\t\t\t", cnt_dict[i][3])
   average += cnt_dict[i][3]
   if(cnt_dict[i][0] == 1):
      mobile += 1

print("Percentage of Mobile users: ",(mobile/n)*100)
print("Average of Time per visit: ",(average/n))