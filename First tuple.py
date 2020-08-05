#Example tuple - tuples are imutable i.e they can't be changed
days_of_week = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')

#Great for programming effeciency and ITEMS can not be changed

#How to use a tuple with image editors
#self.myCanvas.create_text(1, 1, text="Hello World",
#    width=70, fill="blue", anchor="nw",
#    justify="center", font=("Times", 16))

#Define font first and use in multiple instnaces 
# my_font = ("Times", 16)

# self.myCanvas.create_text(50, 50, text="First",
#  font=my_font)
#self.myCanvas.create_text(80, 80, text="Second",
#  font=my_font)

from tkinter import *

class MyFrame(Frame):
  def __init__(self):
     Frame.__init__(self)

     self.myCanvas = Canvas(width=150, height=150, bg="white")
     self.myCanvas.grid()

     self.myCanvas.create_rectangle(10, 10, 20, 20, fill="red")
     self.myCanvas.create_rectangle(10, 30, 20, 40, fill="yellow")
     self.myCanvas.create_rectangle(10, 50, 20, 60, fill="blue")

    # Prints (1,2,3) the tuple for shapes found in the grid
     print ("Finds all shapes")
     print (self.myCanvas.find_enclosed(0, 0, 30, 70))
    # Prints (2,) the tuple for shapes found in the grid
     print ("Finds middle shape")
     print (self.myCanvas.find_enclosed(0, 25, 30, 45))
    # prints () which denotes a tuple
     print ("Finds no shapes")
     print (self.myCanvas.find_enclosed(0, 0, 1, 1) )

frame02 = MyFrame()
frame02.mainloop()
