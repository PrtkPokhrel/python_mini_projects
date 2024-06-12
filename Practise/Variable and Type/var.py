"""
Variable: What are variables?
variables are container to store the data.
a variable can be defined by a unique name , not keywords or reserved words.
the variable also should have a data type like int, float and string.
but for some programming language like python it is not necessary to define the data type.
because in python the data type of the variable is defined by the last value assigned to the variable
unlike java we cannot declare empty variable like int a;
in python simply "a" is considered illegal

"""
# a = "2" + "2"
# print(a)

# Getting input
# the input function always returns string


# hello = input("Enter your name: ")
# print("Your name is ", hello)

# Indexing:
# Parts of string can be accessed through numerical index placed between square brackets

# indexing = "Hello i am index"
# i = 0
# for i in range(9):
#     index = indexing[i]
#     print(index)


# Negative indexing

# nIndexing = "int float"
#
# for i in range(1, 10):
#     index = nIndexing[-i]
#     print(index)


# Slicing the strings:

# strA="This is a string"
# slice=strA[1:4]
# slicingString=strA[-4:-2]
# print(slicingString)
# print(slice)


name=input("Enter your name: ")
if name:
    print("Your name is ", name)
else:
    print("Your name is empty")