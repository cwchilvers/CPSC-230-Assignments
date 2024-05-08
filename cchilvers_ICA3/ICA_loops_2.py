# ask usr for a num

import math

user_num=input("Please Enter a number")


while user_num.isdigit():
        user_num = int(user_num)
        whole_num=math.sqrt(user_num)

        # print if num is perfect square
        if whole_num%1==0:
            whole_num=int(whole_num)
            print("Your number is a perfect square: ", user_num)
            break
        # ask for another num if not perf square
        else:
            print("Sorry your num was not a perfect square")
            user_num=input("try again")
