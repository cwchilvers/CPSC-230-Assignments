# Chandler Chilvers
# 2311765
# cchilvers@chapman.edu
# 230-06
# Battle Game

import random, os, ctypes


# User Info ========================================================= #

user_name = ""
user_health = 0
user_health_bar = ""
user_healths = [30, 50, 100]
user_level = 0
games_won = 0

user_health_bars = ["[|||] ", "[|||||] ", "[||||||||||] "]
user_moves = [("Kick", 1), ("Punch", 5)]
user_wins = 0

# User's accuracy increases with every round won/decreases every round lost
# User's chance of critical hit increase and decrease when winning/losing a round
accuracy_CH_level = 0
user_accuracy = ["75", "80", "82", "86", "90", "94", "96", "99"]
user_critical_hit = ["99", "98", "97", "96", "94", "88", "84", "80"]

user_learn_moves = [("Slap", 12), ("Hyper Beam", 18)]

# Opponent Info ----------------------------------------------------- #

opponent_health = 0
opponent_health_bar = ""
opponent_wins = 0
final_boss = str(os.environ['COMPUTERNAME'])
opponents = [("Billy McRib-Breaker", 20, "[||] "), ("Skull-Crusher", 50, "[|||||] "),
             (final_boss, 200, "[||||||||||||||||||||] ")]

opponent_1_moves = [("Slap", 2), ("Kick", 8), ("Splash", 0)]
opponent_2_moves = [("Slam", 7), ("Crush", 9), ("Punch", 4)]
opponent_3_moves = [("Brute-Force", 12), ("Crunch", 8), ("Spam", 0)]

# Other ------------------------------------------------------------ #

Round = 0
Turn = 0
numbers = "0123456789"


# ========================= Get Info ============================== #


def get_user_health():
    global user_health
    user_health = user_healths[user_level]
    return user_health


def get_user_health_bar():
    global user_health_bar
    user_health_bar = user_health_bars[user_level]
    return user_health_bar


def get_user_accuracy():
    global accuracy_CH_level
    accuracy_chance = int(user_accuracy[accuracy_CH_level])
    return accuracy_chance


def get_opponent_name(opponent_num):
    opponent_list = list(opponents[opponent_num])
    name = opponent_list[0]
    return name


def get_opponent_health(opponent_num):
    opponent_list = list(opponents[opponent_num])
    health = opponent_list[1]
    return health


def get_opponent_health_bar(opponent_num):
    opponent_list = list(opponents[opponent_num])
    health_bar = opponent_list[2]
    return health_bar


def get_new_move():
    global user_moves, user_learn_moves, games_won
    new_move_info = user_learn_moves[games_won - 1]
    user_moves = add_new_move(new_move_info)
    return user_moves


def get_user_CH():
    global accuracy_CH_level
    CH_chance = int(user_accuracy[accuracy_CH_level])
    return CH_chance


# ========================== Display ============================== #


def display_user_moves():
    global user_moves, numbers, user_name
    user_moves_display = user_name + "'s moves: "
    move_number = 0

    for move_tuple in user_moves:
        move_number += 1
        user_moves_display += move_tuple[0] + " (" + (str(move_number)) + ") "
    print(user_moves_display)


def display_health():
    print(user_name, user_health, "HP          vs           ", opponent_name, opponent_health, "HP\n\n")


def new_screen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def enter():
    input("                                            (...)\n")


def double_line():
    print("===============================================================")


def line():
    print("---------------------------------------------------------------")


def display_round_info(opponent_num):
    double_line()
    print("                            ROUND", str(Round), "\n" +
          user_name + ": " + user_health_bar + str(user_health) + "\n"
          + get_opponent_name(opponent_num) + ": " + opponent_health_bar
          + str(opponent_health) + "\n")
    line()


# ============================= Misc. ============================= #


def get_continue():
    Continue = input("Continue?: (Y) (N)\n")
    Continue = str(Continue)
    return Continue

def check_entry(entry):
    status = ""
    symbols = ("!@#$%^&*()_-+=~:;<>,.?/\"[]{}\'")
    for char in entry:
        if char == "" or char in symbols:
            status = "Invalid"
        else:
            status = "Valid"
    return status


def fix_name(name):
    # Capitalize first letter:
    name = name[:1].upper() + name[1:]
    # Eliminate any spaces at end
    name = list(name[::-1])
    for char in range(0, len(name)):
        if name[char] == " ":
            name[char] = ""
        else:
            break
    name = "".join(name)
    name = name[::-1]
    return name


def end_round(opponent_num):
    print("                              K.O.!")
    if user_health > opponent_health:
        global user_wins, user_name, opponent_name, Round, accuracy_CH_level, \
            Room, opponent_wins, user_health_bar, user_healths, \
            games_won, user_health_bars, user_moves, Continue
        user_wins += 1
        accuracy_CH_level += 1
        print(user_name + ": ", user_wins, "\n"
              + opponent_name + ": ", opponent_wins, "\n")
        enter()
        new_screen()
        reset_no_round(opponent_num)
        Round += 1
    else:
        opponent_wins += 1
        if accuracy_CH_level > 0:
            accuracy_CH_level -= 1
        print(user_name + ": ", user_wins, "\n"
              + opponent_name + ": ", opponent_wins, "\n")
        enter()
        new_screen()
        reset_no_round(opponent_num)
        Round += 1

    # End Level
    if Round == 4:
        if Room != 3:
            if user_wins > opponent_wins:
                ctypes.windll.user32.MessageBoxW(0, "Congratulations, You Won!!!", "WINNER!", 0)
                enter()
                new_screen()
                games_won += 1
                increase_user_attacks()
                increase_user_health()
                increase_user_health_bar()
                Round = 1
                line()

                # New move
                print(user_name, "learned a new move.\n")
                user_moves = get_new_move()
                enter()
                display_user_moves()
                enter()
                Round = 1
                Room += 1
                user_wins = 0
                opponent_wins = 0
                new_screen()

            elif opponent_wins > user_wins:
                print("You lose...")
                enter()
                check_continue = True
                while check_continue == True:
                    user_continue = get_continue()
                    # Continue
                    if user_continue.lower() == "yes" or user_continue.lower() == "y":
                        Round = 1
                        Room += 1
                        user_wins = 0
                        opponent_wins = 0
                        new_screen()
                        check_continue = False
                        break
# ==============================================================================         
# ERROR HERE for No Continue: instead of going to Room 4 (which when using print
# says it is indeed set to Room 4), it goes to the next Room anyway for some reason
                    elif user_continue.lower() == "no" or user_continue.lower() == "n":
                        Room = 4
                        user_wins = 0
                        opponent_wins = 0
                        Round = "none"
                        check_continue = False
                        new_screen()
                        break
                    new_screen()
                if Room == 4:
                    Room = 4
            if Room == 4:
                Room = 4
# ==============================================================================


        # End Game
        elif Room == 3:
            if user_wins > opponent_wins:
                new_screen()
                print("If you see this text then congrats! You beat the game!")
                enter()
                new_screen()
                Room = 4
            else:
                new_screen()
                print("LOSER! YOU'RE A LOSER!")
                enter()
                new_screen()
                Room = 4


def update_health_bar(p_hlth, health_bar):
    health_bar = list(health_bar)

    if p_hlth >= 190 and p_hlth < 200:
        for char in range(20, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"
    if p_hlth >= 180 and p_hlth < 190:
        for char in range(19, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"
    if p_hlth >= 170 and p_hlth < 180:
        for char in range(18, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"
    if p_hlth >= 160 and p_hlth < 170:
        for char in range(17, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"
    if p_hlth >= 150 and p_hlth < 160:
        for char in range(16, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"
    if p_hlth >= 140 and p_hlth < 150:
        for char in range(15, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"
    if p_hlth >= 130 and p_hlth < 140:
        for char in range(14, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"
    if p_hlth >= 120 and p_hlth < 130:
        for char in range(13, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"
    if p_hlth >= 110 and p_hlth < 120:
        for char in range(12, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"
    if p_hlth >= 100 and p_hlth < 110:
        for char in range(11, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"
    if p_hlth >= 90 and p_hlth < 100:
        for char in range(10, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"
    if p_hlth >= 80 and p_hlth < 90:
        for char in range(9, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"
    if p_hlth >= 70 and p_hlth < 80:
        for char in range(8, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"
    if p_hlth >= 60 and p_hlth < 70:
        for char in range(7, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"
    if p_hlth >= 50 and p_hlth < 60:
        for char in range(6, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"
    if p_hlth >= 40 and p_hlth < 50:
        for char in range(5, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"
    if p_hlth >= 30 and p_hlth < 40:
        for char in range(4, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"

    if p_hlth >= 20 and p_hlth < 30:
        for char in range(3, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"

    if p_hlth >= 10 and p_hlth < 20:
        for char in range(2, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = "-"

    if p_hlth >= 1 and p_hlth < 10:
        for char in range(2, len(health_bar)):
            if health_bar[char] == "|":
                health_bar[char] = " "
        health_bar[1] = "*"
    health_bar = "".join(health_bar)
    return health_bar


def increase_user_attacks():
    global user_moves, numbers
    new_moves_damage = []
    for group in user_moves:
        group = list(group)
        group[1] += 6
        group = tuple(group)
        new_moves_damage.append(group)
    user_moves = new_moves_damage


def increase_user_health():
    global user_health, user_healths, games_won
    user_health = user_healths[games_won]


def increase_user_health_bar():
    global user_health_bar, user_health_bars, games_won
    user_health_bar = user_health_bars[games_won]


def add_new_move(new_move_info):
    global user_moves
    new_move = new_move_info
    new_user_move = user_moves + [new_move]
    return new_user_move


# ============================= Reset ============================= #


def reset_user_health():
    global user_health, games_won
    user_health = user_healths[games_won]
    return user_health


def reset_user_health_bar():
    global user_health_bar, games_won
    user_health_bar = user_health_bars[games_won]
    return user_health_bar


def reset_opponent_health(opponent_num):
    global opponent_health
    opponent_health = get_opponent_health(opponent_num)
    return opponent_health


def reset_opponent_health_bar(opponent_num):
    global opponent_health_bar
    opponent_health_bar = get_opponent_health_bar(opponent_num)
    return opponent_health_bar


def reset_round():
    global Round
    Round = 1
    return Round


def reset_turn():
    global Turn
    Turn = 0
    return Turn


def reset_wins():
    global user_wins
    user_wins = 0


def reset(opponent_num):
    reset_user_health()
    reset_user_health_bar()
    reset_opponent_health(opponent_num)
    reset_opponent_health_bar(opponent_num)
    reset_round()
    reset_turn()
    reset_wins()


def reset_no_round(opponent_num):
    reset_user_health()
    reset_user_health_bar()
    reset_opponent_health(opponent_num)
    reset_opponent_health_bar(opponent_num)
    reset_turn()


# ============================= Moves ============================= #


def get_selected_move(player_moves, player1, player2):
    global move_name, move_damage
    player_moves_list = list(player_moves[move_select])
    move_name = player_moves_list[0]
    move_damage = player_moves_list[1]
    get_move_type(player1, player2)


def get_move_type(player1, player2):
    global move_select
    normal_moves = ["Punch", "Kick", "Slap", "Slam", "Crush"]
    computer_moves = ["Brute-Force", "Crunch"]
    if move_name in normal_moves:
        normal_attack(player1, player2)
    elif move_name == "Splash":
        splash_attack(player1)
    elif move_name in computer_moves:
        computer_attack(player1, player2)
    elif move_name == "Spam":
        spam()
    elif move_name == "Hyper Beam":
        hyper_beam()


def normal_attack(player1, player2):
    global opponent_health, user_health, move_select, move_damage

    Quit = 0
    verb = ""

    if move_name == "Punch":
        verb = "punched"
    elif move_name == "Kick":
        verb = "kicked"
    elif move_name == "Slap":
        verb = "slapped"
    elif move_name == "Slam":
        verb = "slammed"
    elif move_name == "Crush":
        verb = "crushed"

    new_screen()
    print(player1, verb, player2 + ".\n")
    enter()

    if player1 == user_name:
        accuracy = get_user_accuracy()
        hit_or_miss = random.randint(0, 100)
        # Miss
        if hit_or_miss >= accuracy:
            print("...But missed!")
            enter()
            new_screen()
            Quit = 1

    # Critical Hit
    if player1 == user_name and Quit != 1:
        CH_chance = get_user_CH()
        CH_random = random.randint(0, 100)

        if CH_random >= CH_chance:
            print("SMAAAASH!!")
            CH_damage = random.randint(5,10)
            enter()
            new_screen()
            move_damage += CH_damage

    if player1 == user_name and Quit != 1:
        opponent_health -= move_damage
        print(player2, "took", move_damage, "points in damage.\n")
        enter()
        new_screen()
    elif player1 == opponent_name:
        user_health -= move_damage
        print(player2, "took", move_damage, "points in damage.\n")
        enter()
        new_screen()


def splash_attack(player1):
    new_screen()
    print(player1, "used SPLASH!\n")
    enter()
    print("...But nothing happened!\n")
    enter()
    new_screen()


def computer_attack(player1, player2):
    global move_name, user_health
    new_screen()
    verb = "used"
    print(player1, verb, move_name + ".\n")
    user_health -= move_damage
    enter()
    print(player2, "took", move_damage, "points in damage.\n")
    enter()
    new_screen()


def spam():
    global user_health
    new_screen()
    spam_random = random.randint(0,2)
    if spam_random == 0:
        enter()
        print("\"..." + user_name + "...\"")
        enter()
        new_screen()
        print("\"...go...b...a...c...k...\"")
        enter()
    elif spam_random == 1:
        enter()
        print("\"..." + user_name + "...\"")
        enter()
        new_screen()
        print("You cannot grasp the true form of", final_boss + "'s attack!\n")
        enter()
        new_screen()
        print(user_name, "took 15 points in damage.\n")
        enter()
        user_health -= 15
    elif spam_random == 2:
        enter()
        print("\"..." + user_name + "...\"")
        enter()
        new_screen()
        print("\"" + user_name + ", " + user_name + ", " + user_name + ", " + user_name + ", "
              + user_name + ", "  + user_name + ", " + user_name + ", " + user_name + ", "
              + user_name + ", " + user_name + ",\n"  + user_name + ", " + user_name + ", "
              + user_name + ", " + user_name + ", " + user_name + ", " + user_name + ", "
              + user_name + ", " + user_name + ", " + user_name + ", " + user_name + ", "
              + user_name + ", " + user_name + ", " + user_name + ", " + user_name + ",\n"
              + user_name + ", " + user_name + ", " + user_name + ", " + user_name + ", "
              + user_name + ", " + user_name + ", " + user_name + ", " + user_name + ", "
              + user_name + ", " + user_name + ", " + user_name + ", " + user_name + ", "
              + user_name + ", " + user_name + ",\n" + user_name + ", " + user_name + ", "
              + user_name + ", " + user_name + ".... ")
        enter()
    new_screen()


def hyper_beam():
    global opponent_health
    new_screen()
    print("P E W !\n")
    enter()
    new_screen()
    print("____________________________________________________________________*.\{ * )]/.")
    print("____________________________________________________________________X<{ ^   }>")
    print("                                                                    . /V<V }>\  \n")
    enter()
    new_screen()
    opponent_health -= 18
    print(final_boss, "took 18 points in damage.\n")
    enter()
    new_screen()


# _________________________________________________________________ #
#                             G A M E                               #
# _________________________________________________________________ #

Game = 1
while Game == 1:

    # START SCREEN ---------------------------------------------------- #


    Room = "Start"
    while Room == "Start":

        new_screen()
        # Ask user for name:
        sub_Room = "Ask Name"
        while sub_Room == "Ask Name":
            user_name = input("\"Welcome to Wii Kick Butt. What's your name?:\"\n")
            entry_status = (check_entry(user_name))
            if entry_status == "Valid":
                # Fix name
                user_name = fix_name(user_name)
                sub_Room = "None"
                break
            else:
                new_screen()

        # Dialogue
        print("\n\"" + user_name + ", huh? Duuuude that's a badass name.\"\n")
        input("                                  (...press any key to continue)\n")
        new_screen()

        # Information
        line()
        print("                       Before you begin:\n")
        display_user_moves()
        print("\n - Your moves will be displayed like this on every turn.\n"
              " - Select moves by entering their corresponding numbers.\n")
        enter()
        print(" - Press Q during your turn to quit game.\n")
        input("                                 (...press any key to begin game)\n")
        new_screen()
        print("\n\"Alright. Good luck out there.\"\n")
        enter()
        new_screen()
        break


    # LEVEL 1 ---------------------------------------------------- #


    Room = 1
    reset(0)

    while Room == 1 and Room != 4:
        opponent_name = get_opponent_name(0)

        # Quit
        if Room == "Quit":
            Room = "Quit"
            break
        
        # Skip
        if Room == 4:
            Room = 4
            break
        
        # End round
        if user_health <=0 or opponent_health <= 0:
            end_round(0)
            if Room == 2:
                break
            if Room == 4:
                break

        # User's turn
        while Turn == 0:

            user_health_bar = update_health_bar(user_health, user_health_bar)
            opponent_health_bar = update_health_bar(opponent_health, opponent_health_bar)
            display_round_info(0)
            display_user_moves()

            # User selects attack
            move_select = input("")
            if move_select == "":
                new_screen()
                break
            elif move_select.lower() == "q":
                Room = "Quit"
                break
            for char in move_select:
                if move_select in numbers:
                    move_select = int(move_select)
                    move_select -= 1
                    if move_select in range(0, len(user_moves)):
                        get_selected_move(user_moves, user_name, opponent_name)
                        Turn = 1
                        break
                else:
                    new_screen()
                    break

        # End round
        if user_health <= 0 or opponent_health <= 0:
            end_round(0)
            if Room == 2:
                break
            if Room == 4:
                break

        # Computer's turn
        while Turn == 1:

            # Opponent choses move
            move_select = random.randint(0,len(opponent_1_moves))
            move_select = str(move_select)
            for char in move_select:
                if move_select in numbers:
                    move_select = int(move_select)
                    if move_select in range(0, len(opponent_1_moves)):
                        get_selected_move(opponent_1_moves, opponent_name, user_name)
                        Turn = 0
                        break

    if Room == "Quit":
        break


    # LEVEL 2 ---------------------------------------------------- #


    if Room != "Quit" or Room != 4:
        Room = 2
        reset(1)

    if Room == 2 and Room != 4:
        while Room == 2 and Room != 4:
            opponent_name = get_opponent_name(1)

            # Quit
            if Room == "Quit":
                Room = "Quit"
                break
            
            # Skip
            if Room == 4:
                Room = 4
                break
            
            # End round
            if user_health <=0 or opponent_health <= 0:
                end_round(1)
                if Room == 3:
                    break
                if Room == 4:
                    break
        
            # User's turn
            while Turn == 0:

                user_health_bar = update_health_bar(user_health, user_health_bar)
                opponent_health_bar = update_health_bar(opponent_health, opponent_health_bar)
                display_round_info(1)
                display_user_moves()

                # User selects attack
                move_select = input("")
                if move_select == "":
                    new_screen()
                    break
                elif move_select.lower() == "q":
                    Room = "Quit"
                    break
                for char in move_select:
                    if move_select in numbers:
                        move_select = int(move_select)
                        move_select -= 1
                        if move_select in range(0, len(user_moves)):
                            get_selected_move(user_moves, user_name, opponent_name)
                            Turn = 1
                            break
                    else:
                        new_screen()
                        break

            # End round
            if user_health <= 0 or opponent_health <= 0:
                end_round(1)
                if Room == 3:
                    break
                if Room == 4:
                    break


            # Computer's turn
            while Turn == 1:

                # Opponent chooses move
                move_select = random.randint(0,len(opponent_2_moves))
                move_select = str(move_select)
                for char in move_select:
                    if move_select in numbers:
                        move_select = int(move_select)
                        if move_select in range(0, len(opponent_2_moves)):
                            get_selected_move(opponent_2_moves, opponent_name, user_name)
                            Turn = 0
                            break


    if Room == "Quit":
        break


    # LEVEL 3 ---------------------------------------------------- #


    if Room != "Quit" or Room != 4:
        Room = 3
        reset(2)

    if Room == 3 and Room != 4:
        while Room == 3:
            opponent_name = get_opponent_name(2)

            # Quit
            if Room == "Quit":
                Room = "Quit"
                break
            
            # Skip
            if Room == 4:
                Room = 4
                break

            # End round
            if user_health <=0 or opponent_health <= 0:
                end_round(2)
                if Room == 4:
                    break
                
            # User's turn
            while Turn == 0:

                user_health_bar = update_health_bar(user_health, user_health_bar)
                opponent_health_bar = update_health_bar(opponent_health, opponent_health_bar)
                display_round_info(2)
                display_user_moves()

                # User selects attack
                move_select = input("")
                if move_select == "":
                    new_screen()
                    break
                elif move_select.lower() == "q":
                    Room = "Quit"
                    break

                for char in move_select:
                    if move_select in numbers:
                        move_select = int(move_select)
                        move_select -= 1
                        if move_select in range(0, len(user_moves)):
                            get_selected_move(user_moves, user_name, opponent_name)
                            Turn = 1
                            break
                    else:
                        new_screen()
                        break

            # End round
            if user_health <= 0 or opponent_health <= 0:
                end_round(2)
                if Room == 4:
                    break

            # Computer's turn
            while Turn == 1:

                # Opponent chooses move
                move_select = random.randint(0,len(opponent_3_moves))
                move_select = str(move_select)
                for char in move_select:
                    if move_select in numbers:
                        move_select = int(move_select)
                        if move_select in range(0, len(opponent_3_moves)):
                            get_selected_move(opponent_3_moves, opponent_name, user_name)
                            Turn = 0
                            break


    if Room == "Quit":
        break


    # END ----------------------------------------------------- #

    if Room != "Quit":
        Room = 4

    if Room == 4:
        while Room == 4:
            play_again = input("Play again?: (Y) (N)\n")
            if play_again.lower() == "yes" or play_again.lower() == "y":
                Room = "Start"
                games_won = 0
                user_moves = [("Kick", 3), ("Punch", 5)]
                accuracy_CH_level = 0
                break
            elif play_again.lower() == "no" or play_again.lower() == "n":
                Room = "Quit"
                break
            else:
                new_screen()

    if Room == "Quit":
        break
