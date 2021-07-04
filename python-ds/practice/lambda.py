
func = lambda x,y: x**y
num = int(input('Base Number : '))
power = int(input('Power : '))
value = func(num,power)
print('Base %i and Power %i = %i '%(num,power,value))