# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.

def isEvenOdd(number: int) -> str:
    if number % 2 == 0:
        return "even"
    return "odd"


usernumber = int(input("Veuillez saisir un nombre entier : "))

print("The number you typed is %s." % isEvenOdd(usernumber))
