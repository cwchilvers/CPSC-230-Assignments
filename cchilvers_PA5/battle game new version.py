

user_moves = [("Punch", 3), ("Kick", 4)]

# ================================== Functions ===================================
def get_damage_number(move_number, move_tuple):
    select_move = move_tuple[move_number]
    damage_number = select_move[1]
    return damage_number

def display_user_moves():
    move_display = ""
    move_number = 0
    for move in user_moves:
        for char in move:
            if char.isdigit():
                move_number += 1
                move_display += (" " + "(" + str(move_number) + ") ")
                break
    return move_display
# =================================================================================
    

display_user_moves()
