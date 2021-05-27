#Write the custom function avg() so that it returns the average of the given parameters.


def avg(x , y):
    avg = (x + y) / 2
    return(avg)
 
x = 128
y = 255
z = avg(x,y)
print ("The average of",x,"and", y, "is", z)