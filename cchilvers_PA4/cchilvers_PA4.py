# Chandler Chilvers
# 2311765
# cchilvers@chapman.edu
# 230-06
# Programming Assignment 4: Pig

# =======================================================================================

# import random module

import random

app = 1

game = 0

while app == 1:

    # Quit game
    if app == 0:
        break

    # Intro
    while game == 0:
        usr = input("Play a game of PIG?: (Y/N)\n")

        # reset scores
        usr_score = 0
        comp_score = 0

        # reset turn
        turn = 0

        # reset sum
        usr_sum = 0
        comp_sum = 0

        # Yes
        if usr == "y" or usr == "Y" or usr == "yes" or usr == "YES":
            game = 1
            print("Sweet. Let's roll.\n\n")
            print("=============================================================\n")
            turn = 1.1
            break

        # No (quit)
        elif usr == "no" or usr == "NO" or usr == "n" or usr == "N":
            app = 0
            print("Fine")
            break

        # Typed something invalid
        else:
            print("Im sorry. Let me say that again.\n")

    # Dice Game
    while game == 1:

        # Display score
        print("You:", usr_score, "Computer:", comp_score)

        # When someone wins
        if usr_score >= 100 or comp_score >= 100:
            game = 2
            break

        # User's turn (1st roll)
        while turn == 1.1:
            usr_roll = random.randint(1, 6)
            print("You rolled a", usr_roll, "\n")

            # If rolled a 1
            if usr_roll == 1:
                turn = 2.1
                # Reset user sum for rolls
                usr_sum = 0
                print("=============================================================\n")
                break

            # If rolled number > 1
            else:
                usr_sum += usr_roll
                turn = 1.2
                break

        # User's turn (After 1st roll)
        while turn == 1.2:

            # Prompt user for roll or hold
            usr_input = input("r = roll  h = hold:\n")

            # Roll
            if usr_input == "r" or usr_input == "R":
                usr_roll = random.randint(1,6)
                print("You rolled a", usr_roll, "\n")

                # If rolled a 1
                if usr_roll == 1:
                    turn = 2.1
                    # Reset user sum for rolls
                    usr_sum = 0
                    print("=============================================================\n")
                    break

                # If rolled number > 1
                else:
                    usr_sum += usr_roll

            # Hold
            elif usr_input == "h" or usr_input == "H":
                print("You held\n")
                usr_score += usr_sum
                # Reset user sum for rolls
                usr_sum = 0
                # Set to computer's turn
                turn = 2.1
                print("=============================================================\n")
                break

        # Computer's turn (1st roll)
        while turn == 2.1:

            # reset computer sum for rolls
            comp_sum = 0

            comp_roll = random.randint(1, 6)
            print("I rolled a", comp_roll, "\n")

            # If computer rolls 1
            if comp_roll == 1:
                turn = 1.1
                # Reset comp sum for rolls
                comp_sum = 0
                print("=============================================================\n")
                break

            # If rolled number > 1
            else:
                comp_sum += comp_roll
                turn = 2.2
                break

        # Computer's turn (after 1st roll)
        while turn == 2.2:

            # Roll or hold?
            comp_rh = random.randint(1,100)

            # Roll
            if comp_rh > 45:
                comp_roll = random.randint(1,6)
                print("I rolled a", comp_roll, "\n")

                # If computer rolls 1
                if comp_roll == 1:
                    turn = 1.1
                    # Reset comp sum for rolls
                    comp_sum = 0
                    print("=============================================================\n")
                    break

                # If rolled number > 1
                else:
                    comp_sum += comp_roll

            # Hold
            else:
                print("I held. Your turn.\n")
                comp_score += comp_sum
                # Reset comp sum for rolls
                comp_sum = 0
                # Set to user's turn
                turn = 1.1
                print("=============================================================\n")
                break

    # Ending
    while game == 2:
        if usr_score >= 100:
            print("You win...\n")
            game = 0
            break

        else:
            print("HA! I WIN!\n")
            game = 0
            break
