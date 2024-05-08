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

a = float(a)
b = float(b)
c = float(c)

# Calculate discriminate

d1 = b**2 - 4 * a * c
d2 = b**2 - 4 * a * c

# Check value of discriminant. Warn if value is negative

if d1 < 0:
    print("WARNING: Negative discriminant! Do NOT continue at all costs!")
          
else:
    r1 = (-b + math.sqrt(d1)) / (2 * a)
    r2 = (-b - math.sqrt(d2)) / (2 * a)

    # cast

    r1 = float(r1)
    r2 = float(r2)

    # print

    print(r1, r2)
