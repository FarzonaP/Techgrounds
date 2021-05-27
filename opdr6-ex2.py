#Write a custom function myfunction() that prints “Hello, world!” to the terminal. Call myfunction.
#Rewrite your function so that it takes a string as an argument. Then, it should print “Hello, <string>!”.

def my_function(fname):
    print("Hello " + fname)

my_function(input("What's your name? "))