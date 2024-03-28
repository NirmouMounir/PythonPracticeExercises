# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

from datetime import date

inputname = input("Please enter your name : ")
inputage = int(input("Please enter your age : "))
ageyear = date.today().year + (100 - inputage)
ntimes = int(input("Now, enter a random number from 1 to 10 : "))
result = (f"Hello %s, you will turn 100yo in %i" % (inputname, ageyear))

# for i in range(ntimes):
#     print(result)

print(ntimes * (result + "\n"))
