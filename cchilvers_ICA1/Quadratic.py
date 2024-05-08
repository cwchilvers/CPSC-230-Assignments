# Chandler Chilvers
# 2311765
# cchilvers@chapman.edu
# 230-06
# Quadratic

import math

# prompt usr for coefficients a, b, c

a = input("a: ")
b = input("b: ")
c = input("c: ")

# cast

a = int(a)
b = int(b)
c = int(c)

# Calculate

r1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
r2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)

# cast

r1 = int(r1)
r2 = int(r2)

# print

print(r1,r2)

