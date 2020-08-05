from tkinter import *
from time import *
import time

Movelist = {"Move1":0, "Move2": 0, "Move3":0, "Move4":0,
                "Move5":0, "Move6":0,"Move7":0, "Move8":0, "Move9":0}

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



    

        
        
z = 0
def CheckRange(num, z2):
    if num in range(number1, number2):
        print ("you have selected a correct number")
        global z
        z = z + z2
        return z*z2
    else:
        print (" This simply will not do")



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
        while Movelist ['Move1'] == 0:
            z = 0
            while z == 0:
                y = 0
                while y == 0:
                    num = input("Please input your move 1-9: ")
                    try:
                        val = int(num)
                        y = y + 1
                    except ValueError:
                        print (num, 'is Not a number')
                num = int(num)
                CheckRange(num, 1)
            num = str(num)
            move = 'X'+num
            
            if WinCondition [move] == "X":
                print ("You already have that spot")

            elif errorcheck [move] == 0:
                errorcheck [move] = 1
                WinCondition [move] = "X"
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
                    
                elif move == "X9":
                    X27 = self.myCanvas.create_line(320,300,400,375, width=2)
                    X28 = self.myCanvas.create_line(320,375,400,300, width=2)
                    

                else:
                    print ("Not a correct move")
                self.myCanvas.update()
                move = 'O'+num
                errorcheck [move] = 1
                Movelist ['Move1'] = 1
                z = 0
                y = 0

            elif move in errorcheck == 1:
                print ("Seats Taken")                             

            
            else:
                print ("How did you even get this error?")
#AI Turn to move                 
        ai = 0
        while Movelist ['Move2'] == 0:
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
                                                    print ("This is the final move")
                                                    ai = ai +1
                                            else:
                                                move = 'O5'
                                                print('I have made my move')
                                                time.sleep(1)
                                                ai = ai + 1
                                        else:
                                            move = 'O6'
                                            print('I have made my move')
                                            time.sleep(1)
                                            ai = ai + 1
                                        
                                    else:
                                        move = 'O4'
                                        print('I have made my move')
                                        time.sleep(1)
                                        ai = ai + 1
                                else:
                                    move = 'O8'
                                    print('I have made my move')
                                    time.sleep(1)
                                    ai = ai + 1
                            else:
                                move = 'O1'
                                print('I have made my move')
                                time.sleep(1)
                                ai = ai + 1
                        else: 
                            move = 'O1'
                            print ('I have made my move')
                            time.sleep(2)
                            ai = ai + 1
                    else:
                        move = 'O7'
                        print ('I have made my move')
                        time.sleep(2)
                        ai = ai + 1
                    
                    
                else:
                    move = 'O9'
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
                        
            elif move == "O9":
                O19 = self.myCanvas.create_oval(320,300,400,375, width=2)
                   

            self.myCanvas.update()
            Movelist ['Move2'] = 1

#Make your second move
        while Movelist ['Move3'] == 0:
            while z == 0:
                y = 0
                while y == 0:
                    num = input("Please input your move 1-9: ")
                    try:
                        val = int(num)
                        y = y + 1
                    except ValueError:
                        print (num, 'is Not a number')
                num = int(num)
                CheckRange(num)
                z = z + 1
            num = str(num)
            move = 'X'+num
                        
            if WinCondition [move] == "X":
                print ("You already have that spot")
                z = 0
                y = 0

            elif errorcheck [move] == 0:
                errorcheck [move] = 1
                WinCondition [move] = "X"
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
                    
                elif move == "X9":
                    X27 = self.myCanvas.create_line(320,300,400,375, width=2)
                    X28 = self.myCanvas.create_line(320,375,400,300, width=2)
                    

                else:
                    print ("Not a correct move")
                self.myCanvas.update()
                move = 'O'+num
                errorcheck [move] = 1
                Movelist ['Move3'] = 1
                z = 0
                y = 0

            elif move in errorcheck == 1:
                print ("Seats Taken")                             

            
            else:
                print ("How did you even get this error?")


#AI Turn to move                 
        ai = 0
        while Movelist ['Move4'] == 0:
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
                                                    print ("This is the final move")
                                                    ai = ai +1
                                            else:
                                                move = 'O5'
                                                print('I have made my move')
                                                time.sleep(1)
                                                ai = ai + 1
                                        else:
                                            move = 'O6'
                                            print('I have made my move')
                                            time.sleep(1)
                                            ai = ai + 1
                                        
                                    else:
                                        move = 'O4'
                                        print('I have made my move')
                                        time.sleep(1)
                                        ai = ai + 1
                                else:
                                    move = 'O8'
                                    print('I have made my move')
                                    time.sleep(1)
                                    ai = ai + 1
                            else:
                                move = 'O1'
                                print('I have made my move')
                                time.sleep(1)
                                ai = ai + 1
                        else: 
                            move = 'O1'
                            print ('I have made my move')
                            time.sleep(2)
                            ai = ai + 1
                    else:
                        move = 'O7'
                        print ('I have made my move')
                        time.sleep(2)
                        ai = ai + 1
                    
                    
                else:
                    move = 'O9'
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
                        
            elif move == "O9":
                O19 = self.myCanvas.create_oval(320,300,400,375, width=2)
                   

            self.myCanvas.update()
            Movelist ['Move4'] = 1
           
 
                
        

        
        
        
frame01 = ttt()
frame01.mainloop()
