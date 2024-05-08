import random

# user info
user_name = ""
user_health = 30
user_moves = [("kick", 2), ("Punch", 5)]

opponents = [("Bob", 15), ("Joe", 30), ("Greg", 140)]

# ================================================================ #

def get_opponent_name(index_num):
    opponent_list = list(opponents[index_num])
    name = opponent_list[0]
    return name

def get_opponent_health(index_num):
    opponent_list = list(opponents[index_num])
    health = opponent_list[1]
    return health

def display_user_moves():
    numbers = "0123456789"
    user_moves_display = ""
    move_number = 0
    for move in user_moves:
        for char in move:
            char_string = str(char)
            if char_string not in numbers:
                user_moves_display += char
            elif char_string in numbers:
                move_number += 1
                user_moves_display += (" (" + str(move_number) + ") ")
    return print(user_moves_display)

def display_health():
    print(user_name, user_health, "HP          vs           ", opponent_name, opponent_health, "HP\n\n")


def new_screen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def enter():
    input("                                  (...)\n")

    
opponent_name = (get_opponent_name(0))
opponent_health = (get_opponent_health(0))
display_user_moves()
enter()
new_screen()
display_health()
