# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.pe

def isAMultipleOf(number: int, div: int) -> str:
    if number % div == 0:
        return "Number %i is a multiple of %i" % (number, div)
    return "Number %i is not a multiple of %i" % (number, div)


numberone = int(input("Veuillez saisir un premier nombre entier : "))
numbertwo = int(input("Veuillez saisir un deuxième nombre entier : "))

print(isAMultipleOf(numberone, numbertwo))
