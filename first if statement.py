# First If statement ever
age = 10
if age != 10:
    print ("TEN")
print ("Hows That?")

# Showing that you can do < and > for strings and Captilized is before lower case
letter = "C"
if letter < "a":
    print ("less than a")

if letter > "B":
    print ("Greater than B")

# First test and inputing to an if statment to result in true or false with else
age = int(input("Inpute your age\n"))
if age >= 18:
    print ("You are able to vote")
else:
    print ("you are not able to vote")

# Multiple input and answer if statements
year = eval(input("Enter year: "))
if year == 1:
   print ("Freshman")
if year == 2:
   print ("Sophomore")
if year == 3:
   print ("Junior")
if year == 4:
   print ("Senior")

# Nesting the else and if statements

year = int(input("Enter Year: "))
if year == 1:
    print ("Freshmen")
else:
   if year == 2:
        print ("sophmore")
   else:
      if year == 3:
            print ("junior")
      else:
         if year == 4:
                print ("senior")

# Same as abobe now instead using elif in replace of else and if

year = int(input("Enter School Year: "))
if year == 1:
   print ("freshmen")
elif year == 2:
   print ("sophmore")
elif year == 3:
   print ("junior")
elif year == 4:
   print ("senior")
else:
   print ("not a valid number")

                
