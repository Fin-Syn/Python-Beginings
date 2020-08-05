from tkinter import *
from time import *

class Myframe(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.myCanvas = Canvas(width=300, height=200, bg="white")
        self.myCanvas.grid()

        my_rect_id = self.myCanvas.create_rectangle (10, 10, 50, 50)
        self.myCanvas.update()

        for count in range(10):
            increment = 10*count
            self.myCanvas.coords(my_rect_id, 10 + increment,
                                 10 + increment, 50 + increment,
                                 50 + increment)
            self.myCanvas.update()
            sleep(1)
        



        #for count in range(10):
            #increment = 10*count
            #self.myCanvas.create_rectangle(10 + increment,
            #                               10 + increment, 50 + increment,
             #                              50 + increment)
            #self.myCanvas.update()
            #sleep(1)

           # self.myCanvas.create_rectangle(10 + increment,
            #                                 10 + increment, 50 + increment, 50 + increment,
           #                                  outline="white")

        #self.myCanvas.create_rectangle (10, 10, 200, 100, fill="green",
        #                               outline="purple", width= 5)
        #self.myCanvas.update()

        #sleep(1)

        #self.myCanvas.create_rectangle (50, 50, 200, 100, fill="blue",
                                        #outline="cyan", width= 5)

        #self.myCanvas.create_oval (10,10,200,100, fill="white")

        #self.myCanvas.create_line (1, 1, 200, 200, arrow="first", fill="cyan",
                                   #width=3)

        #self.myCanvas.create_text(75, 30, text="Hello World", width=70,
                                  #fill="blue", anchor="w", justify="right",
                                  #font=("Times", 16))

        
        

frame02 = Myframe()
frame02.mainloop()
