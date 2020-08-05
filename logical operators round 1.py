# Logical operators

age = int(input("how old are you? "))
registered = input("Are you registered?: (y/n) ")

if age >= 18 and registered == "y" or registered == "Y" or registered == "Yes" or registered == "yes":
   print(" Your are ready to vote")
else:
   print (" You are not ready to vote")


# Simple Hourly Calculator and wage

wage = float(input('Please input your wage: '))
hours = float(input('Please input number of hours worked this week: '))

if hours <= 40:
   print (hours * wage)
elif hours > 40:
   pay = ("Your pay is $")
   print (pay,(((hours - 40) * (wage * 1.5)) + (wage * 40)))
else:
   print ("Not valid")

