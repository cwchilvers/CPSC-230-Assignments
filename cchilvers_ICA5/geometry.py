# Chandler Chilvers
# 2311765
# cchilvers@chapman.edu
# 230-06
# Geometry

import math

pi = math.pi

def calc_area(r):
    A = pi * math.sqrt(r)
    return A

def calc_circ(r):
    C = 2 * pi * r
    return C
    
def calc_vol(r, h):
    V = calc_area(r) * h
    return V

# get usr input
r = input("Radius:\n")
r = float(r)
h = input("Height:\n")
h = float(h)

circle_A = calc_area(r)
print("Area: " + str(circle_A))

circle_C = calc_circ(r)
print("Circumference: " + str(circle_C))

cylinder_V = calc_vol(r, h)
print("Volume: " + str(cylinder_V))
