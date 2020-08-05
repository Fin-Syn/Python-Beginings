# Huricane wind speed Assignment 3

print ("Sooooooo.... you have yourself a huricane")
Wind_speed = int(input("Please enter wind speed "))

if Wind_speed > 74 and Wind_speed < 95:
   print ("You havee yourself a KITTIE 1 Huricane....Be safe")
elif Wind_speed > 94 and Wind_speed < 111:
   print ("DAMMMN.... that is a KITTIE 2 Hiricane....Good lawdy")
elif Wind_speed > 110 and Wind_speed < 131:
   print ("SOB.... KITTIE 3 in effect.....find cover")
elif Wind_speed > 130 and Wind_speed < 156:
   print ("RUUUUNNNNN there are 4 KITTTIES.....you are doomed")
elif Wind_speed > 156:
   print ("5 KIITTES...there is nothing left to say")
else:
   print("Why are you wasting my time")


# Takes advantage of the fact that once the condtion is met it will
# print the answer, I.E 99 less than 75, no, continuem less than 95.
# No continue. Less than 110 Yes, print, condition met, exit. 

speed = eval(input("Please enter the wind speed: "))

if speed < 74:
    print ("This is not a hurricane")
elif speed <= 95:
    print ("Category 1")
elif speed <= 110:
    print ("Category 2")
elif speed <= 130:
    print ("Category 3")
elif speed <= 155:
    print ("Category 4")
else:
    print ("Category 5")
