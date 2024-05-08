# Chandler Chilvers
# 2311765
# cchilvers@chapman.edu
# 230-06
# Practice Loops 2


# prompt usr for how many num they would like to sum

sum_num = input("How many numbers do you want to add?\n")
sum_num = int(sum_num)

# set sum

sum = 0
# ask usr for each num
for index in range(0, sum_num):
    chose_num = input("Enter number for " + str(index + 1) + ":")
    #cast
    chose_num = int(chose_num)
    # add new num to sum
    sum += chose_num

# display sum
print(sum)
