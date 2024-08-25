def plantSunflowers():
	x, y, sun_start, index, max_petals_num, m_petals = 0, 0, 0, 0, 0, 0
	sun_goal = get_world_size() ** 2
	l_sun_pos, l_petals, l_sunHarvest, l_x_y, l_x_y_petals, l_to_test = [], [], [], [], [], []
	petals = measure()

	for i in range(get_world_size()):
		for j in range(get_world_size()):
			tillIfNeeded()
			plant(Entities.Sunflower)
			watering()
			if can_harvest():
				#get pos & measure
				x, y = get_pos_x(), get_pos_y()
				m_petals = measure()
				
				l_x_y_petals = [x,y,m_petals]
				l_to_test.append(l_x_y_petals)

				if l_sun_pos in l_to_test:
					pass
				else:
					l_x_y = [l_x_y_petals[0],l_x_y_petals[1]]
					l_sun_pos.append(l_x_y)
					l_petals.append(l_x_y_petals[2])
				sun_start = len(l_sun_pos)
				
			if sun_start == sun_goal - 1:
				while len(l_petals) > 0:
					if len(l_petals) > 0:
						max_petals_num = max(l_petals)
					else:
						max_petals_num = l_petals[0]
					if max_petals_num in l_petals:
						while (max_petals_num != l_petals[index]):
							index += 1
						l_sunHarvest = l_sun_pos[index]

					g_x, g_y = l_sunHarvest[0], l_sunHarvest[1]
					
					while (g_x != x or g_y != y):
						x, y = get_pos_x(), get_pos_y()
						actual_petals = measure()
						if (x != g_x):
							if (x < g_x):
								move(East)
							else:
								move(West)
						elif (y != g_y):
							if (y < g_y):
								move(North)
							else:
								move(South)
						elif (x == g_x and y == g_y and actual_petals == max_petals_num):
							harvest()

					l_petals.pop(index)
					l_sun_pos.pop(index)
					index = 0
			move(North)
		move(East)