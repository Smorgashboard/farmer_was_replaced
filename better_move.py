def better_move(dest_x, dest_y):
    curr_x = get_pos_x()
    curr_y = get_pos_y()
    while curr_x < dest_x :
        move(East)
        curr_x = get_pos_x()
    while curr_x > dest_x:
        move(West)
        curr_x = get_pos_x()
    while curr_y < dest_y :
        move(North)
        curr_y = get_pos_y()
    while curr_y > dest_y:
        move(South)
        curr_y = get_pos_y()
