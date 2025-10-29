import better_move

def make_dict():
    cact_dict = {}
    
def make_field(cactus_list):
    for x in cactus_list:
            better_move.better_move(x[0], x[1])
            if get_entity_type() != Entities.Cactus or get_entity_type() != None:
                harvest()
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Cactus)

def drone_cactus():
    change_hat(Hats.Cactus_Hat)
    cactus_list = []
    sorted = False
    fully_grown = False
    cact_dict_grown = {}
    
    for x in range(0,6):
        for y in range(13,32):
            cactus_list.append((x,y))
    
    make_field(cactus_list)
        
    while fully_grown == False:
        for x in cactus_list:
            better_move.better_move(x[0],x[1])
            if can_harvest():
                cact_dict_grown[(x[0],x[1])] = True
                
        for x in cact_dict_grown:
            if cact_dict_grown[x] == False:
                break
            else:
                fully_grown = True
                
    while fully_grown == True:
        iters = 0
        swaped = False
        for x in cactus_list:
            better_move.better_move(x[0],x[1])
            curr_val = measure()
            north_val = measure(North)
            east_val = measure(East)
            if north_val != None:
                if curr_val > north_val:
                    swap(North)
                    swaped = True
            if east_val != None:    
                if curr_val > east_val:
                    swap(East)
                    swaped = True
        if swaped == False:
            sorted = True
            fully_grown = False
                
    if sorted == True:
        harvest()
        
                
                   
