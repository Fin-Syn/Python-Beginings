# Creating my first loop

number = 1
while number <= 5:
   print (number)
   number = number + 1
print ("Thats all folks")

number = 1
answer = 'y'
while answer == 'y' or answer == 'yes':
   print (number)
   number = number + 1
   answer = input(
       "Do you want to see the next number, 'y/n'\n")

# My first for loop averager

num = eval(input("How many numbers do you want to average: "))

sum = 0.0
for x in range(num, 0, -1):
   value = eval(input("Enter a value: "))
   sum = sum + value

average = sum / num
print ("The average is:", average)
