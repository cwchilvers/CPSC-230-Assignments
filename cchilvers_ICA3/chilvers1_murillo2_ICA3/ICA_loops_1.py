# Chandler Chilvers
# 2311765
# cchilvers@chapman.edu
# 230-06
# ICA Loops 1

# ask for variable

x = input("Enter an integer: \n")

x = int(x)

int_sum = 0

# find sum of x consec. int.

for consecutive in range(1, x+1, 1):
    int_sum=int_sum+consecutive
    print("consecutive is:", consecutive)

print("The sum is:", int_sum)
