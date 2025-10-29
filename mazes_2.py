import better_move

def solve():
	treasure_cord = measure()
	solving = True
	directions = [North, East, South, West]
	index = 0
	visted = set()
	while solving:
		if get_entity_type() == Entities.Treasure:
			harvest()
			solving = False
		else:
			if can_move(directions[(index + 1) %4 ]):
				index = (index + 1) % 4
				move(directions[index])
			elif can_move(directions[index]):
				move(directions[index])
			elif can_move(directions[(index - 1) % 4]):
				index = (index - 1) % 4
			elif can_move(directions[(index + 2) % 4]):
				index = (index + 2) % 4
				
			
				

def test_maze():
	
	mazes_cords = []
	for x in range(22, 32):
		for y in range(0, 10):
			mazes_cords.append((x,y))
	while True:
		better_move.better_move(27, 5)
		plant(Entities.Bush)
		use_item(Items.Weird_Substance, 40)
		solve()
