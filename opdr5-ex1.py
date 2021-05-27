#Use the input() function to ask the user of your script for their name.
#If the name they input is your name, print a personalized welcome message.
#If not, print a different personalized message.


a = "Aous"

name = input('Please input your name: ')
if name == a:
    print('Hello! Welcome here, ' + name + '!')

else:
    print('You are ' + name + ', not ' + a + '. Please leave. Thank you and goodbye!')
