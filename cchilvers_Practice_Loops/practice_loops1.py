# Chandler Chilvers
# 2311765
# cchilvers@chapman.edu
# 230-06
# Practice Loops 1


# ask usr for int

usr_num = input("Gimme an integer:\n")
usr_num = int(usr_num)

# loop to print every even digit between 0 and input

for index in range(0, usr_num):
    if index % 2 != 0:
        continue
    print(index)


print("\n")


# another loop for every digit divisible by 5 from 0 to input

for index2 in range(0, usr_num):
    if index2 % 5 == 0:
        print(index2)