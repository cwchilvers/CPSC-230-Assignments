import os, random

Game = 1
Mode = 1
Level = 0
Round = 1
Turn = 0
critical_hit = 0

numbers = "0123456789"

# User
user_moves = [("Punch", 5), ("Kick", 6)]
user_health = 50
user_health_bar = "[|||||] "
user_name = ""
user_wins = 0

# friends
friends = []

# Opponents
opponent_health_bar = "[|||] "
opponent_name = ""
opponent_health = 0
opponent_wins = 0
final_boss = str(os.environ['COMPUTERNAME'])
opponents = [("Bobby McRib-Breaker", 30), ("Skull Crusher", 40), ("Greg"), (final_boss)]

# Opponent Moves
BMRB_moves = [("Slap", 2), ("Kick", 7), ("Splash", 0)]
SC_moves = [("Slam", 6), ("Crush", 7)]


# ================================== Functions ===================================

def get_damage_number(move_number, move_tuple):
    select_move = move_tuple[move_number]
    damage_number = select_move[1]
    return damage_number


def get_opponent_health(opponent_number):
    health_number = opponents[opponent_number]
    health_number = health_number[1]
    return health_number


def get_opponent_name(opponent_number):
    opp_name = opponents[opponent_number]
    opp_name = opp_name[0]
    return opp_name


def display_user_moves():
    numbers = "0123456789"
    move_display = ""
    move_number = 0
    for move in user_moves:
        for char in move:
            char_string = str(char)
            if char_string not in numbers:
                move_display += char
            elif char_string in numbers:
                move_number += 1
                move_display += (" (" + str(move_number) + ") ")
    return print(move_display)


def enter():
    return input("                                                        (...)")


def space():
    return print("\n")


def line():
    return print("\n===================================================================\n")


def line_thin():
    return print("\n-------------------------------------------------------------------\n")


def display_round_info():
    return print("\n===================================================================\n"
                 + "                            ROUND " + str(Round) + "\n"
                 + user_name + ": " + user_health_bar + str(user_health)
                 + "    -=| vs |=-    "
                 + opponent_name + ": " + opponent_health_bar + str(opponent_health) + "\n"
                 + "\n--------------------------------------------------------------------\n")


def normal_attack(p1, p2, verb, p2_health):
    print(p1, verb, p2 + " took " + str(damage) + " points in damage.\n")
    p2_health -= damage
    return p2_health


def attack(p1, p2, p1_moves, p2_health):
    p1_move = p1_moves[select_move_num]
    p1_move = p1_move[0]

    if p1_move == "Punch":
        verb = "punched."
        return normal_attack(p1, p2, verb, p2_health)

    elif p1_move == "Kick":
        verb = "kicked."
        return normal_attack(p1, p2, verb, p2_health)

    elif p1_move == "Slap":
        verb = "slapped."
        return normal_attack(p1, p2, verb, p2_health)


def splash_attack(p1):
    print(p1 + " used SPLASH!\n")
    enter()
    print("...But nothing happened!\n")


def critical_hit_attack(p2_health):
    critical_hit_damage = random.randint(10, 20)
    p2_health -= critical_hit_damage
    print("SMAAAASH!! " + opponent_name + " took " + str(critical_hit_damage) + " points in damage!")
    return p2_health


def update_health_bar(health_bar, p_hlth):
    health_bar = list(health_bar)

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


def get_moves_length():
    moves_length = len(user_moves)
    return moves_length


def big_space():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


# =================================================================================

while Game == 1:

    if Game == 0:
        break

    # Start Screen
    while Mode == 1:

        select = input("\"Welcome to Wii Kick Butt. How tough are ya?\": \n\n"
                       "(1) = \"How tough am I? HOW TOUGH AM I?!?\"\n(2) = \"How tough am I? You got a new bottle of ketchup?\"\n\n")

        if select == str(1):
            print("\"Uh... right this way. Sorry to keep you waiting.\"\n\n")
            input("                                (...Press any key to continue)")
            big_space()
            line()
            enter_name = 1

            while enter_name == 1:
                # enter name
                user_name = input("What's your name? \n")
                user_name = str(user_name)
                # make first letter uppercase
                user_name = user_name[:1].upper() + user_name[1:]
                # eliminate spaces at end
                user_name = user_name[::-1]
                user_name = list(user_name)
                for char in range(0, len(user_name)):
                    if user_name[char] == " ":
                        user_name[char] = ""
                    else:
                        break
                user_name = "".join(user_name)
                user_name = user_name[::-1]
                if user_name != "":
                    enter_name = 0
                    break

            space()

            print("\"" + user_name + "? Dude, that's a badass name.\"")
            enter()

            big_space()

            line_thin()
            print("                          Before you begin:\n")
            print("\nMoves will be displayed before each battle.")
            enter()
            print("Select moves by entering their corresponding numbers.\n")
            display_user_moves()
            enter()
            print("Press Q anytime to quit.\n")
            enter()
            ready_to_start = 1
            while ready_to_start == 1:
                start_game = input("Press S to if you're ready to start game:\n")
                if start_game == "s" or start_game == "S":
                    line_thin()
                    print("\n\"Alright. Good luck out there.\"\n")
                    big_space()

                    # Get opponent name and health
                    opponent_name = get_opponent_name(0)
                    opponent_health = get_opponent_health(0)

                    Mode = 2
                    Level = 1
                    ready_to_start = 0
                    break

                elif start_game == "Q" or start_game == "q":
                    game = 0
                    line()
                    print("\"Get outta here. This place is too tough for you.\"")
                    enter()
                    ready_to_start = 0
                    break

        elif select == str(2):
            print("\"Get outta here. This place is too tough for you.\"")
            enter()
            Game = 0
            break

    # Level 1
    while Level == 1:

        if Game == 0:
            break

        if Level == 2:
            break

        # End Round
        if user_health <= 0 or opponent_health <= 0:
            big_space()
            print("                            K.O.!\n")
            if user_health > opponent_health:
                print(user_name + " + 1\n")
                opponent_health = get_opponent_health(0)
                opponent_health_bar = "[|||] "
                user_health = 50
                user_health_bar = "[|||||] "
                user_wins += 1
                enter()
                Round += 1
                Level = 1
                big_space()
                break

            elif opponent_health_health > user_health:
                print(opponent_name + " + 1\n")
                opponent_health = get_opponent_health(0)
                opponent_health_bar = "[|||] "
                user_health = 50
                user_health_bar = "[|||||] "
                opponent_wins += 1
                enter()
                Round += 1
                Level = 1
                big_space()
                break

        # After 3 rounds
        while Round == 4:
            if user_wins > opponent_wins:
                print("You won!")
                enter()
                print("...")
                enter()
                print("Quick! Throw your Poké Ball!")
                input("                        ( ...press any key to throw Poké Ball)\n")
                print(opponent_name + ": \"What? NO! WAIT!\"")
                enter()
                print(user_name + " used a Poké Ball.")
                enter()
                print("...")
                enter()
                opponent_name = opponent_name.upper()
                print("Gotcha! " + opponent_name + " was caught!")
                enter()
                nickname_mode = 1
                while nickname_mode == 1:
                    nickname_select = input("Give a nickname to " + opponent_name + "?: (Y) (N)\n")
                    if nickname_select.lower() == "y" or nickname_select.lower() == "yes":
                        line()
                        nickname = input("Enter a nickame for " + opponent_name + ":\n")
                        nickname = str(nickname)
                        # make first letter uppercase
                        nickname = nickname[:1].upper() + nickname[1:]
                        # eliminate spaces at end
                        nickname = nickname[::-1]
                        nickname = list(nickname)
                        for char in range(0, len(nickname)):
                            if nickname[char] == " ":
                                nickname[char] = ""
                            else:
                                break
                        nickname = "".join(nickname)
                        nickname = nickname[::-1]

                        if nickname != "":
                            # change name and add to friends
                            insert_name = opponents[0]
                            insert_name = list(insert_name)
                            insert_name[0] = nickname
                            insert_name = tuple(insert_name)
                            friends.append(insert_name[0])

                            print(friends[0] + " was sent to " + final_boss + "\n")
                            enter()
                            big_space()
                            nickname_mode = 0

                            Level = 2
                            Round = 1
                            # Get opponent name and health
                            opponent_name = get_opponent_name(1)
                            opponent_health = get_opponent_health(1)
                            opponent_health_bar = "[||||] "
                            break

                    elif nickname_select.lower() == "n" or nickname_select.lower() == "no":
                        nickname_mode = 0

                        # add to PC
                        insert_name = opponents[0]
                        friends.append(insert_name[0])

                        print(friends[0] + " was sent to " + final_boss + "\n")
                        enter()
                        big_space()
                        nickname_mode = 0

                        Level = 2
                        Round = 1
                        # Get opponent name and health
                        opponent_name = get_opponent_name(1)
                        opponent_health = get_opponent_health(1)
                        opponent_health_bar = "[||||] "
                        break
                break

            else:
                print(opponent_name, "kicked your butt!")
                enter()
                big_space()

                # Get opponent name and health
                opponent_name = get_opponent_name(1)
                opponent_health = get_opponent_health(1)
                opponent_health_bar = "[||||] "
                break

        # User's turn
        while Turn == 0 and Round != 4:

            # Update health bars
            user_health_bar = update_health_bar(user_health_bar, user_health)
            opponent_health_bar = update_health_bar(opponent_health_bar, opponent_health)

            # Display round information
            display_round_info()

            # Display moves
            display_user_moves()

            # Select move
            select_move_num = str(input(""))

            # Quit
            if select_move_num == "q" or select_move_num == "Q":
                big_space()
                line()
                print("What's a synonym for " + user_name + "?... \n\nLOSER.")
                enter()
                Game = 0
                break

            # check if input makes sense
            elif select_move_num.isdigit():
                select_move_num = int(select_move_num)

                if select_move_num not in range(1, get_moves_length() + 1):
                    Turn = 0
                    break
            else:
                Turn = 0
                break

            # Normal Attacks
            if select_move_num >= 1 or select_move_num <= 2:
                select_move_num -= 1

                # Critical Hit
                critical_hit = random.randint(0, 100)

                if critical_hit >= 95:
                    opponent_health = critical_hit_attack(opponent_health)

                    enter()
                    Turn = 1
                    break

                # If not critical hit
                else:
                    # get damage number
                    damage = get_damage_number(select_move_num, user_moves)

                    # change opponent health
                    opponent_health = attack(user_name, opponent_name, user_moves, opponent_health)

                    enter()
                    Turn = 1
                    break

        # Opponent's Turn
        while Turn == 1 and Round != 4:
            select_move_num = random.randint(1, 3)

            if 1 <= select_move_num <= 2:
                select_move_num -= 1

                # get damage number
                damage = get_damage_number(select_move_num, BMRB_moves)

                # change user health
                user_health = attack(opponent_name, user_name, BMRB_moves, user_health)

                enter()
                big_space()
                Turn = 0
                break

            elif select_move_num == 3:
                splash_attack(opponent_name)
                enter()
                big_space()
                Turn = 0
                break
        break

# ----------------------------------------------------------------------------------
    # Level 2
    while Level == 2:

        if Game == 0:
            break

        if Level == 2:
            break

        # End Round
        if user_health <= 0 or opponent_health <= 0:
            big_space()
            print("                            K.O.!\n")
            if user_health > opponent_health:
                print(user_name + " + 1\n")
                opponent_health = get_opponent_health(1)
                opponent_health_bar = "[|||] "
                user_health = 50
                user_health_bar = "[|||||] "
                user_wins += 1
                enter()
                Round += 1
                Level = 2
                big_space()
                break

            elif opponent_health_health > user_health:
                print(opponent_name + " + 1\n")
                opponent_health = get_opponent_health(1)
                opponent_health_bar = "[|||] "
                user_health = 50
                user_health_bar = "[|||||] "
                opponent_wins += 1
                enter()
                Round += 1
                Level = 2
                big_space()
                break

        # After 3 rounds
        while Round == 4:
            if user_wins > opponent_wins:
                print("You won!")
                enter()
                print("...")
                enter()
                print("Quick! Throw your Poké Ball!")
                input("                        ( ...press any key to throw Poké Ball)\n")
                print(opponent_name + ": \"What? NO! WAIT!\"")
                enter()
                print(user_name + " used a Poké Ball.")
                enter()
                print("...")
                enter()
                opponent_name = opponent_name.upper()
                print("Gotcha! " + opponent_name + " was caught!")
                enter()
                nickname_mode = 1
                while nickname_mode == 1:
                    nickname_select = input("Give a nickname to " + opponent_name + "?: (Y) (N)\n")
                    if nickname_select.lower() == "y" or nickname_select.lower() == "yes":
                        line()
                        nickname = input("Enter a nickame for " + opponent_name + ":\n")
                        nickname = str(nickname)
                        # make first letter uppercase
                        nickname = nickname[:1].upper() + nickname[1:]
                        # eliminate spaces at end
                        nickname = nickname[::-1]
                        nickname = list(nickname)
                        for char in range(0, len(nickname)):
                            if nickname[char] == " ":
                                nickname[char] = ""
                            else:
                                break
                        nickname = "".join(nickname)
                        nickname = nickname[::-1]

                        if nickname != "":
                            # change name and add to friends
                            insert_name = opponents[1]
                            insert_name = list(insert_name)
                            insert_name[0] = nickname
                            insert_name = tuple(insert_name)
                            friends.append(insert_name[0])

                            print(friends[1] + " was sent to " + final_boss + "\n")
                            enter()
                            big_space()
                            nickname_mode = 0

                            Level = 2
                            break

                    elif nickname_select.lower() == "n" or nickname_select.lower() == "no":
                        nickname_mode = 0

                        # add to PC
                        insert_name = opponents[1]
                        friends.append(insert_name[0])

                        print(friends[1] + " was sent to " + final_boss + "\n")
                        enter()
                        big_space()
                        nickname_mode = 0

                        Round = 1
                        Level = 2

                        # Get opponent name and health
                        opponent_name = get_opponent_name(1)
                        opponent_health = get_opponent_health(1)
                        opponent_health_bar = "[||||] "
                        break
                break

            else:
                print(opponent_name, "kicked your butt!")
                enter()
                big_space()

                Round = 1
                Level = 2

                # Get opponent name and health
                opponent_name = get_opponent_name(1)
                opponent_health = get_opponent_health(1)
                opponent_health_bar = "[||||] "
                break

        # User's turn
        while Turn == 0 and Round != 4:

            # Update health bars
            user_health_bar = update_health_bar(user_health_bar, user_health)
            opponent_health_bar = update_health_bar(opponent_health_bar, opponent_health)

            # Display round information
            display_round_info()

            # Display moves
            display_user_moves()

            # Select move
            select_move_num = str(input(""))

            # Quit
            if select_move_num == "q" or select_move_num == "Q":
                big_space()
                line()
                print("What's a synonym for " + user_name + "?... \n\nLOSER.")
                enter()
                Game = 0
                break

            # check if input makes sense
            elif select_move_num.isdigit():
                select_move_num = int(select_move_num)

                if select_move_num not in range(1, get_moves_length() + 1):
                    Turn = 0
                    break
            else:
                Turn = 0
                break

            # Normal Attacks
            if select_move_num >= 1 or select_move_num <= 2:
                select_move_num -= 1

                # Critical Hit
                critical_hit = random.randint(0, 100)

                if critical_hit >= 95:
                    opponent_health = critical_hit_attack(opponent_health)

                    enter()
                    Turn = 1
                    break

                # If not critical hit
                else:
                    # get damage number
                    damage = get_damage_number(select_move_num, user_moves)

                    # change opponent health
                    opponent_health = attack(user_name, opponent_name, user_moves, opponent_health)

                    enter()
                    Turn = 1
                    break

        # Opponent's Turn
        while Turn == 1 and Round != 4:
            select_move_num = random.randint(1, 3)

            if 1 <= select_move_num <= 2:
                select_move_num -= 1

                # get damage number
                damage = get_damage_number(select_move_num, SC_moves)

                # change user health
                user_health = attack(opponent_name, user_name, SC_moves, user_health)

                enter()
                big_space()
                Turn = 0
                Level = 2
                break
        break
    break
# ------------------------------------------------------------------------------------

