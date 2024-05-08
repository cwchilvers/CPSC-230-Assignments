import random, os

game = 1
mode = 1
level = 0
turn = 0
round = 1

# define user's moves and health
usr_moves = [("Punch, 3"), ("Kick, 4")]
usr_health = 50
usr_bar = "[|||||] "

# opponents
opp_bar = "[|||] "
final_boss = str(os.environ['COMPUTERNAME'])
opponents = [("Bobby McRib-Breaker"), ("Skull Crusher"), ("Greg"), (final_boss)]
bmrb_hlth = 30
bmrb_moves = [("Slap, 2"), ("Kick, 7"), ("Splash, 0")]
sc_hlth = 40
greg_hlth = 50
fb_hlth = 100

# ============================== define functions ================================ #

def display_moves():
    move_display = ""
    move_display_num = 0

    # Retrieve move name only
    for move in usr_moves:
        for char in move:
            if char != ",":
                move_display += char
            elif char == ",":
                move_display_num += 1
                move_display += (" " + "(" + str(move_display_num) + ") ")
                break
    return str(move_display)

def damage_number(m, s):
    move = m[s]
    num = ""
    nums = "1234567890"
    for char in move:
        if char in nums:
            num += char
    num = int(num)
    num = num - 1
    num = str(num)
    return num

def display_round_info(u, x, a, b):
    return print("===================================================================\n"
    + "                            ROUND " + str(round) + "\n"
    + usr_name + ": " + a + str(u) + "    -=| vs |=-    "
    + opp_name + ": " + b + str(x) + "\n"
    + "-------------------------------------------------------------------\n")

def update_opp_bar(x, y):
    y = list(y)
    if x >= 30 and x < 40:
        for char in range(4, len(y)):
            if y[char] == "|":
                y[char] = "-"
    elif x >= 20 and x < 30:
        for char in range(3, len(y)):
            if y[char] == "|":
                y[char] = "-"
    elif x >= 10 and x < 20:
        for char in range(2, len(y)):
            if y[char] == "|":
                y[char] = "-"
    elif x >= 1 and x < 10:
        for char in range(2, len(y)):
            if y[char] == "|":
                y[char] = " "
        y[1] = "*"
    y = "".join(y)
    return y

def update_usr_bar(x, z):
    z = list(z)
    if x == 50:
        for char in range(6, len(z)):
            if z[char] == "|":
                z[char] = "-"
    elif x >= 40 and x < 50:
        for char in range(5, len(z)):
            if z[char] == "|":
                z[char] = "-"
    elif x >= 30 and x < 40:
        for char in range(4, len(z)):
            if z[char] == "|":
                z[char] = "-"
    elif x >= 20 and x < 30:
        for char in range(3, len(z)):
            if z[char] == "|":
                z[char] = "-"
    elif x >= 10 and x < 20:
        for char in range(2, len(z)):
            if z[char] == "|":
                z[char] = "-"
    elif x >= 1 and x < 10:
        for char in range(2, len(y)):
            if y[char] == "|":
                y[char] = " "
    z = "".join(z)
    return z

def update_bars(a, b):
    # update health bars
    b = update_opp_bar(bmrb_hlth, b)
    a = update_usr_bar(usr_health, a)
    if turn == 0:
        display_round_info(usr_health, bmrb_hlth, a, b)
    return

# ================================================================================ #

while game == 1:

    if game == 0:
        break

    # Select screen
    while mode == 1:

        select = input("\"Welcome to Wii Kick Butt. How tough are ya?\": \n\n"
        "(1) = \"How tough am I? HOW TOUGH AM I?!?\"\n(2) = \"How tough am I? You got a new bottle of ketchup?\"\n\n")

        if select == str(1):
            print("\"Uh... right this way. Sorry to keep you waiting.\"\n\n")
            input("                                (...Press any key to continue)")
            print("\n===================================================================\n")

            # enter name
            usr_name = input("Enter your name: \n")
            usr_name = str(usr_name)
            usr_name = usr_name[:1].upper() + usr_name[1:]

            print("===================================================================")
            print("\n* Moves will be displayed before each battle. *")
            input("                                                        (...)")
            print("* Select moves by entering their corresponding numbers *")
            mode = 2
            break

        elif select == str(2):
            print("\"Get outta here. This place is too tough for you.\"")
            game = 0
            break

    # Introduction
    while mode == 2:
        usr_moves_display = display_moves()
        print(usr_name +"\'s known moves: " + usr_moves_display + "\n")
        input("                                                        (...)")
        print("* Quit game anytime by pressing (q) * \n")
        input("                                                        (...)")
        start_game = input("Press (s) to start game: \n")
        start_game = str(start_game)

        if start_game == "s" or start_game == "S":
            level = 1
            break

        elif start_game == "Q" or start_game == "q":
            game = 0
            print("===================================================================\n")
            print("What's a synonym for " + usr_name + "?... \n\nLOSER.")
            input("                                                        (...)")
            break

    # Level 1
    while level == 1:
        opp_name = opponents[level]

        # user's turn
        while turn == 0:

            # update health bars
            update_bars(usr_bar, opp_bar)

            usr_moves_display = display_moves()
            usr_select = input(usr_name + "\'s known moves: " + usr_moves_display + "\n")
            usr_select = int(usr_select)
            usr_select = usr_select - 1
            print("\n")

            # if user selects 1 (punch)
            if usr_select == 1:
                damage = damage_number(usr_moves, usr_select)
                print(usr_name + " punched. " + opp_name + " took " + damage +
                      " points in damage.\n")
                damage = int(damage)
                bmrb_hlth -= damage
                input("                                                        (...)")
                turn = 1
                break

            # if user selects 2 (kick)
            elif usr_select == 2:
                damage = damage_number(usr_moves, usr_select)
                print(usr_name + " kicked. " + opp_name + " took " + damage +
                    " points in damage.\n")
                damage = int(damage)
                bmrb_hlth -= damage
                input("                                                        (...)")
                turn = 1
                break

        # opponent's turn
        while turn == 1:

            # update health bars
            update_bars(usr_bar, opp_bar)

            # random move
            opp_move = random.randrange(0, len(bmrb_moves))

            # slap
            if opp_move == 0:
                damage = damage_number(bmrb_moves, opp_move)
                print(opp_name + " slapped " + usr_name + ". " + usr_name + " took " + damage +
                      " points in damage.\n")
                damage = int(damage)
                usr_health -= damage
                input("                                                        (...)")
                turn = 0
                break

            elif opp_move == 1:
                damage = damage_number(bmrb_moves, opp_move)
                print(opp_name + " kicked " + usr_name + ". " + usr_name + " took " + damage +
                      " points in damage.\n")
                damage = int(damage)
                usr_health -= damage
                input("                                                        (...)")
                turn = 0
                break

            # splash
            elif opp_move == 2:
                damage = damage_number(bmrb_moves, opp_move)
                print(opp_name + " used SPLASH!\n" + "...But nothing happened!\n")
                input("                                                        (...)")
                turn = 0
                break
