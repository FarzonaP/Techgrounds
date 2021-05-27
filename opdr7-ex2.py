#Create a list of five integers.
#Use a for loop to do the following for every item in the list:
#Print the value of that item added to the value of the next item in the list. If it is the last item, add it to the value of the first item instead (since there is no next item).

#The first result above is created by adding 9 and 80. The second result is created by adding 80 and 16, etc. The last result is created by adding 35 and 9.

numbers = [9, 80, 16, 67, 35]
print("My list", numbers)
i = 1

for nums in numbers:

    if i > 4:
        b = numbers[0] + numbers[4]
        print(b)
        break

    x = nums
    y = numbers[i]
    a = x + y
    print(a)
    i += 1


#Refaat
# numbers = [3, 6, 9, 12, 15]
# print("Mijn getallen:", numbers)

# for i in range(len(numbers)):
#     print(numbers[i]+numbers[i+1] if i < len(numbers)-1 else numbers[-1]+numbers[0])
