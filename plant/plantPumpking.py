def plantPumpking():
	l_check = []
	l_x_y = []
	pumpking_start = len(l_check) 
	pumpking_goal = get_world_size() ** 2
	if (pumpking_start < pumpking_goal):
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if get_entity_type() != Entities.Pumpkin:
					verifiedHarvest()
				plant(Entities.Pumpkin)
				tillIfNeeded()
				if can_harvest():
					if get_entity_type() == Entities.Pumpkin:
						x, y = get_pos_x(), get_pos_y()
						pumpking_start = len(l_check)
						l_x_y = [x,y]
						if l_x_y not in l_check:
							l_check.append(l_x_y[1])
						l_x_y = []
						if pumpking_start == pumpking_goal-1:
							harvest()
				move(North)
			move(East)