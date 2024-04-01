a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Extras:
#
# 1- Instead of printing the elements one by one, make a new list
# that has all the elements less than 5 from this list in it
# and print out this new list.

# 2- Write this in one line of Python.

# 3- Ask the user for a number and return a list that contains only elements
# from the original list a that are smaller than that number given by the user.

# ---- 1 ----
new_list = []
for nb in a:
    if nb < 5:
        new_list.append(nb)

print(new_list)

# ---- 2 ----
newlist = [number for number in a if number < 5]
print(newlist)
# or print([number for number in a if number < 5])


# ---- 3 ----
usrnb = int(input("Please enter a number : "))
print([lnb for lnb in a if lnb < usrnb])
