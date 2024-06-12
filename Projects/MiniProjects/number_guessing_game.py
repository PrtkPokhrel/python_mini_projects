# Write a python program to guess the number and in how many tries user guess the number4

import random

print("Welcome to the number guessing game!")
numberGuess=0
while 1:
    userNumber=int(input("Guess the number between 1 and 10:"))
    randomNumber=random.randint(0,11)
    if userNumber==randomNumber:
        print("You guessed correctly!")
        print("The number was " + str(userNumber))
        print("You guessed in ",numberGuess," tries")
        break
    else:
        print("Incorrect")
        numberGuess=numberGuess+1
