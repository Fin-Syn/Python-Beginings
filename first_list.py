days_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']

print (days_of_week [2])

#Changes element in the list
days_of_week [0] = 'Sunday'

print (days_of_week)

#Slices the list, but formats is as stated in the list
print (days_of_week [2:5])


#Example nested list, when printing needs to call list, then item within list
child1 = ['Pat', 5, 6.5]
family = [child1]
print (family [0] [1])

kevin_list = []

#Adding single values to a list
kevin_list.append ('kevin')
kevin_list.append ('wolf')

print (kevin_list)

#Adding multiple values to a list in one line of code
kevin_list.extend (['july 26', 29])

print (kevin_list)

#Second way of adding multiple lines to a list
kevin_list = kevin_list + [1991, 'learning python']

#Insert a value in the selected spot
kevin_list.insert (3, 'age')

print (kevin_list)

#Removes only the first instance of selected vaule
kevin_list.remove ('age')

print (kevin_list)

#(max () ) prints highest value in list
number = [16, 8, 15, 42, 23, 4]
print (max(number))

#Automatically sorts list based on pythons defualt, sort can be configured 
number.sort()
print (number)

#Reverses the order of the list
kevin_list.reverse()
print (kevin_list)
