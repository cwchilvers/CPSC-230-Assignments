# Chandler Chilvers, Andrew Orellana
# 2311765
# cchilvers@chapman.edu, orell105@chapman.edu
# 230-06
# ICA 4

from itertools import permutations
import random

words = ("cool", "awesome", "sweet", "houses", "horses", "homies", "computer",
         "science", "ninety", "letters", "screens", "thirty", "fourty",
         "fifty", "sixty", "seventy", "eighty", "hundred", "twenty")

ran_num = 0

tries = 0

# generate random numbers (words 1 - 20)
ran_num = random.randrange(0, 20)

# pick random word from list
word = words[ran_num]

# .join to join together elements of a list
perms = ["".join(p) for p in permutations(word)]

# generate another random number from 1 to length of list
ran_num = random.randrange(1, len(perms))

# select random permutation
ran_perm = perms[ran_num]

# display
print(ran_perm)

while tries <3:
    guess = input("Guess the original word: ")
    if guess == word:
        print("Correct", word)
        break
    else:
        tries += 1
        continue
    break


