for number in range(1, 11):
   if number == 4:
                   break 
   print (number)
else:
   print ("Thanks!")


phrase = input("Enter a phrase: ")
letter = input("Enter a letter: ")
length = len(phrase)

for index in range(0, length):
         if phrase [index] == letter:
                   break
else:
         print ("Your letter wasn't found")



for i in range(0, 10):
         print ("~~~", i, "~~~")
         for j in range(1, 10):
                   print (i*j)
         print ( )
