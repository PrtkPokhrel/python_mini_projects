"""

Given an integer, , perform the following conditional actions:
If is odd, print Weird
If is even and in the inclusive range of 2 to 5, print Not Weird
If is even and in the inclusive range of 6 to 20, print Weird
If is even and greater than 20, print Not Weird
"""

"""n = 24
if n % 2 != 0:
    print("Odd")
elif n % 2 == 0 and (2 <= n <= 5):
    print("Not weird")  

elif n % 2 == 0 and (6 <= n <= 20):
    print("weird")

elif n % 2 == 0 and n >= 20:
    print("Not weird")
"""


def first():
    n = 3

    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not weird")
    else:
        print("Not Weird")

