def direction(facing, turn):
    # your smart code here
    direction_list = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

    if facing not in direction_list:
        return f'Not correct "facing". Set him from list of values ' \
               f'{" ".join(direction_list)}'
    if type(turn) != int and (-1080 > turn or 1080 < turn) or turn % 45 != 0:
        return '"turn" must be integer, between -1080 and 1080 and multiples ' \
               '45 '
    current_direction = direction_list.index(facing)
    new_direction = (turn//45 + current_direction) % 8
    return direction_list[new_direction]
