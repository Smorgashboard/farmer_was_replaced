def make_dict():
    pump_dict = {}
    
    for x in range(0, 6):
        for y in range(0, 6):
            pump_dict[(x,y)] = False
    
    return pump_dict

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
    if get_ground_type() != Grounds.Soil:
        till()


def pumpkin_handling():
    pump_harv = False
    change_hat(Hats.Wizard_Hat)
    pump_dict = make_dict()
    while True:
        if pump_harv == True:
            if get_pos_x() == 5 and get_pos_y() == 5:
                better_move(0,0)
            harvest()
            pump_harv = False
            pump_dict = make_dict()
        for x in pump_dict:
            if pump_dict[x] == False:
                dest_x, dest_y = x[0],x[1]
                better_move(dest_x, dest_y)
                if get_entity_type() != Entities.Pumpkin and get_entity_type() != Entities.Dead_Pumpkin:
                    harvest()
                    plant(Entities.Pumpkin)
                if get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == None:
                    plant(Entities.Pumpkin)
                elif get_entity_type() == Entities.Pumpkin:
                    pump_dict[x] = True
        for x in pump_dict:
            if pump_dict[x] == False:
                break
            else:
                pump_harv = True
                
            
