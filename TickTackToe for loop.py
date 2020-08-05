from tkinter import *
from time import *
import time

Movelist = {1: 0, 2: 0, 3: 0, 4: 0,
                5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

WinCondition = {"X1":"", "X2":"", "X3":"", "X4":"",
                "X5":"", "X6":"","X7":"", "X8":"", "X9":"",
                "O1":"", "O2":"", "O3":"", "O4":"", "O5":"",
                "O6":"","O7":"", "O8":"", "O9":""}

errorcheck = {"X1":0, "X2":0, "X3":0, "X4":0,
                "X5":0, "X6":0,"X7":0, "X8":0, "X9":0,
                "O1":0, "O2":0, "O3":0, "O4":0,"O5":0,
                "O6":0,"O7":0, "":0, "O9":0}

Winner = 0
checkvalue = 0





number1 = 1
number2 = 10



    




def X_Move(self, move):
    if move == "X1":
        self.myCanvas.create_line(90,63,160,145, width=2)
        self.myCanvas.create_line(90,145,160,63, width=2)
                    
    elif move == "X2":
        self.myCanvas.create_line(200,63,280,145, width=2)
        self.myCanvas.create_line(200,145,280,63, width=2)
                    
    elif move == "X3":
        self.myCanvas.create_line(320,63,400,145, width=2)
        self.myCanvas.create_line(320,145,400,63, width=2)
                    
    elif move == "X4":
         self.myCanvas.create_line(90,200,160,275, width=2)
         self.myCanvas.create_line(90,275,160,200, width=2)
                    
    elif move == "X5":
        self.myCanvas.create_line(200,200,280,275, width=2)
        self.myCanvas.create_line(200,275,280,200, width=2)
                    
    elif move == "X6":
         self.myCanvas.create_line(320,200,400,275, width=2)
         self.myCanvas.create_line(320,275,400,200, width=2)
                    
    elif move == "X7":
         self.myCanvas.create_line(90,300,160,375, width=2)
         self.myCanvas.create_line(90,375,160,300, width=2)
                    
    elif move == "X8":
        X25 = self.myCanvas.create_line(200,300,280,375, width=2)
        X26 = self.myCanvas.create_line(200,375,280,300, width=2)
                    
    else:
        move == "X9"
        X27 = self.myCanvas.create_line(320,300,400,375, width=2)
        X28 = self.myCanvas.create_line(320,375,400,300, width=2)

    


class ttt(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.myCanvas = Canvas(width=500, height=500, bg="white")
        self.myCanvas.grid()

        self.myCanvas.create_line(175, 50, 175,400, width=2, fill="black")
        self.myCanvas.create_line(300, 50, 300,400, width=2, fill="black")
        self.myCanvas.create_line(75, 165, 405 ,165, width=2, fill="black")
        self.myCanvas.create_line(75, 285, 405 ,285, width=2, fill="black")
        self.myCanvas.create_rectangle (75, 50, 405, 400)

        


#Make the first moove
        i = 0
        turn = 1
        z = 0
        y = 0
        while i == 0:
            if y < 10:
                while Movelist [turn] == 0:
                    while z == 0:
                        num = input("Pick a number 1-9: ")
                        try:
                            val = int(num)
                            num = int(num)
                        except ValueError:
                            print (num, 'is not a number')
                        else:
                            if num in range(number1, number2):
                                print (' you have chosen number: ',num)
                                z = z + 1
                            else:
                                print ("That is not a valid number")
                
                    num = str(num)
                    move = 'X'+num
            
                    if WinCondition [move] == "X":
                        print ("You already have that spot")
                        z = z - 1

                    elif errorcheck [move] == 0:
                        errorcheck [move] = 1
                        WinCondition [move] = "X"
                        X_Move(self, move)
                        move = 'O'+num
                        errorcheck [move] = 1
                        Movelist [turn] = 1
                        turn = turn + 1
                        print (turn)
                        z = 0
                        y = 0
                    else:
                        print ("Not a vlid move")

               

                    self.myCanvas.update()
                
  
                           
           

#AI Turn to move                 
                    ai = 0
                    while Movelist [turn] == 0:
                        while ai == 0:
                            if errorcheck ['O9'] == 1:
                                print ("I am thinking")
                                time.sleep(1)
                                if errorcheck ['O7'] == 1:
                                    print ("I am thinking")
                                    time.sleep(1)
                                    if errorcheck ['O1'] == 1:
                                        print( "I am thinking")
                                        time.sleep(1)
                                        if errorcheck ['O3'] == 1:
                                            print ('I am thinking')
                                            time.sleep(1)
                                            if errorcheck ['O8'] == 1:
                                                print ('I am thinking')
                                                time.sleep(1)
                                                if errorcheck ['O4'] == 1:
                                                    print ('I am thinking')
                                                    time.sleep(1)
                                                    if errorcheck ['O6'] == 1:
                                                        print ('I am thinking')
                                                        time.sleep(1)
                                                        if errorcheck ['O5'] == 1:
                                                            print ('I am thinking')
                                                            time.sleep(1)
                                                            if errorcheck ['O2'] == 1:
                                                                print ('This was the final move')
                                                                time.sleep(1)
                                                            else:
                                                                move = 'O2'
                                                                num = 2
                                                                print ("This is the final move")
                                                                ai = ai +1
                                                        else:
                                                            move = 'O5'
                                                            num = 7
                                                            print('I have made my move')
                                                            time.sleep(1)
                                                            ai = ai + 1
                                                    else:
                                                        move = 'O6'
                                                        num = 6
                                                        print('I have made my move')
                                                        time.sleep(1)
                                                        ai = ai + 1
                                        
                                                else:
                                                    move = 'O4'
                                                    num = 4
                                                    print('I have made my move')
                                                    time.sleep(1)
                                                    ai = ai + 1
                                            else:
                                                move = 'O8'
                                                num = 8
                                                print('I have made my move')
                                                time.sleep(1)
                                                ai = ai + 1
                                        else:
                                            move = 'O3'
                                            num = 3
                                            print('I have made my move')
                                            time.sleep(1)
                                            ai = ai + 1
                                    else: 
                                        move = 'O1'
                                        num = 1
                                        print ('I have made my move')
                                        time.sleep(2)
                                        ai = ai + 1
                                else:
                                    move = 'O7'
                                    num = 7
                                    print ('I have made my move')
                                    time.sleep(2)
                                    ai = ai + 1
                    
                    
                            else:
                                move = 'O9'
                                num = 9
                                print ('I have made my move')
                                time.sleep(2)
                                ai = ai + 1
                                        
                            if move == "O1":
                                O11 = self.myCanvas.create_oval(90,63,160,145, width=2)
 
                    
                            elif move == "O2":
                                O12 = self.myCanvas.create_oval(200,63,280,145, width=2)
  
                        
                            elif move == "O3":
                                O13 = self.myCanvas.create_oval(320,63,400,145, width=2)

                        
                            elif move == "O4":
                                O14 = self.myCanvas.create_oval(90,200,160,275, width=2)
 
                        
                            elif move == "O5":
                                O15 = self.myCanvas.create_oval(200,200,280,275, width=2)
 
                        
                            elif move == "O6":
                                O16 = self.myCanvas.create_oval(320,200,400,275, width=2)
   
                        
                            elif move == "O7":
                                O17 = self.myCanvas.create_oval(90,300,160,375, width=2)
  
                        
                            elif move == "O8":
                                O18 = self.myCanvas.create_oval(200,300,280,375, width=2)
        
                        
                            else:
                                O19 = self.myCanvas.create_oval(320,300,400,375, width=2)
                        

                    errorcheck [move] == 0
                    errorcheck [move] = 1
                    WinCondition [move] = "O"
                    num = str(num)
                    move = 'X'+num
                    WinCondition [move] = "X"
                    errorcheck [move] = 1
                    Movelist [turn] = 1
                    z = 0
                    y = 0
                    turn = turn + 1
                    self.myCanvas.update()
            else:
                i = i + 1

                
            
frame01 = ttt()
frame01.mainloop()
