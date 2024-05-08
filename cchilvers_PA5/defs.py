user_moves = [("Punch", 3), ("Kick", 4)]

def get_damage_number(move_number, move_tuple):
    select_move = move_tuple[move_number]
    damage_number = select_move[1]
    return damage_number

user_move_select = 1
damage = get_damage_number(user_move_select-1, user_moves)
print(damage)
