# from math import *
#
# print("The square root of 4 is: " ,sqrt(4))

# write a program to find out whether the number is maximum or not(two number)

def maxNumber(a, b):  # function with parameter
    if a > b:
        return a
    else:
        return b


a = int(input("Enter a number: "))
b = int(input("Enter the second number: "))
print(maxNumber(a, b))  # providing argument to the function with parameter
# arguments are also called actual parameters

    
