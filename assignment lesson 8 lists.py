import statistics 
n = 0
numbers = []
while n != (-999):
    number = int(input('Plese Input a number, -999 quits: '))
    if number == -999:
        n = -999
    else:
        numbers = numbers + [number]

print ('The numbers you wanted avaeraged')    

for i in range(len(numbers)):
        # Note the end = " " at the end will keep the output on
        #   the same line
        print (numbers[i], end = " ")

print ('\nThe average is: ',statistics.mean(numbers))
