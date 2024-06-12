import random

userScore = 0
computerScore = 0
while True:

    computer = ['rock', 'paper', 'scissor']
    computerChoice = random.choice(computer)
    userInput = input("Enter r/p/s for rock/paper/scissor or q to quit: ").lower().strip()

    if userInput == 'q':
        print("Thanks for playing")
        print("The score was Computer:", computerScore, "User:", userScore)
        break

    if userInput == 'r' or userInput == 'p' or userInput == 's':
        if (userInput == 'r' and computerChoice == 'rock') or \
                (userInput == 'p' and computerChoice == 'paper') or \
                (userInput == 's' and computerChoice == 'scissor'):
            print("It's a tie")
        elif (userInput == 'r' and computerChoice == 'scissor') or \
                (userInput == 'p' and computerChoice == 'rock') or \
                (userInput == 's' and computerChoice == 'paper'):
            print("You won")
            userScore += 1
        else:
            print("Computer won")
            computerScore += 1

        print("Computer entered", computerChoice)
    else:
        print("Invalid input, please enter r, p, s, or q.")
