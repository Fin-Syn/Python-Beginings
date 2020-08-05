Movelist = {"Move1":0, "Move2": 0, "Move3":0, "Move4":0,
                "Move5":0, "Move6":0,"Move7":0, "Move8":0, "Move9":0}

WinCondition = {"X1":"", "X2":"", "X3":"", "X4":"",
                "X5":"", "X6":"","X7":"", "X8":"", "X9":"",
                "O1":"", "O2":"", "O3":"", "O4":"", "O5":"",
                "O6":"","O7":"", "O8":"", "O9":""}

errorcheck = {"X1":0, "X2":0, "X3":0, "X4":0,
                "X5":0, "X6":0,"X7":0, "X8":0, "X9":1,
                "O1":0, "O2":0, "O3":0, "O4":0,"O5":0,
                "O6":0,"O7":0, "":0, "O9":1}

Winner = 0

#WinCondition ['MC'] = "X"

#print (WinCondition ['MC'])

#if Movelist ['Move2'] == 0:
#    print ("True")
#else:
#    print ("False")

#for moves in (Movelist):
#    move = (input("Select Where you want your X to go: "))
#    if move in WinCondition1:
#        print ("True")
#    else:
#        print ('False')



import time
while Movelist ['Move2'] == 0:
    if errorcheck ['O9'] or errorcheck ['X9'] == 1:
        print ("I am thinking")
        time.sleep(3)
    else:
        move = O9
        print ("Ihave made my move")
    
    
       
   


