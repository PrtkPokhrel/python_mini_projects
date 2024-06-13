print("Welcome to the int float quiz")

userChoice = input("Do you want to play the quiz game (y or n): ")
score = 0
if userChoice.lower() == 'y':
    print("Welcome to the int float quiz game")

    for i in range(1):
        qsn1 = input("What is the full form of CPU: ")
        qsn1 = qsn1.strip()
        qsn1 = qsn1.lower()
        if qsn1 == 'central processing unit':
            score = score + 1

        qsn2 = input("What is the full form of Ip address?: ")
        qsn2 = qsn2.lower()
        qsn2 = qsn2.strip()
        if qsn2 == 'internet protocol address':
            score = score + 1

else:
    print("Exiting the game")

print("Your final score is", score)

