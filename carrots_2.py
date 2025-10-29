import better_move

def drone_carrots():
	carrots_space = []
	for x in range(6, 16):
		for y in range(0, 6):
			carrots_space.append((x,y))

	while True:
		for x in carrots_space:
			better_move.better_move(x[0], x[1])
		
			if get_ground_type() != Grounds.Soil:
				till()
			if get_entity_type() != Entities.Carrot:
				harvest()
				plant(Entities.Carrot)
			else:
				harvest()
				plant(Entities.Carrot)	
		
