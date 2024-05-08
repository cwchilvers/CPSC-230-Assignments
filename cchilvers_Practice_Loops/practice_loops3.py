# Chandler Chilvers
# 2311765
# cchilvers@chapman.edu
# 230-06
# Practice Loops 3

app = True

while app == True:

    import random

    Game = 0

    # reset game
    while Game == 0:
        num = random.randint(1, 10)
        print("Guess my number, between 1 - 10. If you give up, type \"end\"")
        print(num)
        Game = 1

    # game
    while Game == 1:
        guess = input(": ")
        if guess != "end" or guess == "End":
            guess = int(guess)
            if guess == num:
                Game = 2
                break
        elif guess == "end" or guess == "End":
            print("FINE! My number was " + str(num) + "...")
            app = False
            break

    # beat game
    while Game == 2:
        again = input("Yay! Play again? (Y/N")
        if again == "Y" or again == "y":
            Game = 0
            break
        elif again == "n" or again == "N":
            print("See ya!")
            app = False
            break
