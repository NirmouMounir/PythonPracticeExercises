import random

# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = [random.randrange(1, 100) for x in range(28)]
print(a)
b = [random.randint(1, 100) for y in range(50)]
print(b)

res = []
for i in a:
    if i in b:
        res.append(i)

res = list(set(res))
print(res)

res2 = list(set(a).intersection(set(b)))
print(res2)
