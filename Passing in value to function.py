def print_value(value, value2):
    """This function defines a value passed in"""
    print ('Your value is:', value)
    print (value2)

def change_value(value):
    """The function changes the value passed in to 1"""
    value = 1
    print ('Inside, value is changes to: ', value)

number = 5
print ('outisde number is: ', number)
change_value(number)
print ('Outside number is now: ', number)

def changenumber():
    """Globally change number"""
    global number
    number = 'moose'

number = 5
print (number)
changenumber()
print (number)
