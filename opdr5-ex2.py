#Ask the user of your script for a number. Give them a response based on whether the number is higher than, lower than, or equal to 100.

a = 100

number = int(input("Please input a number:"))

if number == a:
    print("100 is a nice number indeed!")

elif number < a:
    print(str(number) + " is pretty low, isn't it?")

else:
    print("Wow, " + str(number) + " is a big number!")


#Or this solution:


#variable
a = 100

#Ask the user of your script for a number.
number = int(input("Please input a number:"))

#Give them a response based on whether the number is equal to 100
if number == a:
    print("100 is a nice number indeed!")

if number > a:
    print("Wow, ", number , " is a big number!")

if number < a:
    print(number, " is pretty low, isn't it?")
    
