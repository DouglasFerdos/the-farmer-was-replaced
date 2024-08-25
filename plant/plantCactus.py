def plantCactus():
	returnToSpawn()
	l_cactiCounter = []
	l_xy = []
	while (num_items(Items.Cactus) < 50000 and len(l_cactiCounter) < 100):
		for i in range(get_world_size()):
			l_xy = [get_pos_x(), get_pos_y()]
			if l_xy not in l_cactiCounter:
				l_cactiCounter.append(l_xy)
			tillIfNeeded()
			plant(Entities.Cactus)
			move(East)
		move(North)