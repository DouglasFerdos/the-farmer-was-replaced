def cactus_columnSort():
	l_mc = []
	for i in range(get_world_size()):
		l_mc.append(measure())
		move(North)
	s = len(l_mc)
	
	for i in range(s):
		swapped = False
	
		for j in range(s-1):
			if (l_mc[j] > l_mc[j+1]):
				temp = l_mc[j]
				l_mc[j] = l_mc[j+1]
				l_mc[j+1] = temp
				swapped = True
				swap(North)
				move(North)
			elif (get_pos_y() < (s-i-1)):
				move(North)
		#goToPos
		g_y = 0
		y = get_pos_y()
		while (g_y != y):
			y = get_pos_y()
			if (y != g_y):
				if (y < g_y):
					move(North)
				else:
					move(South)
	
		while (get_pos_y() != 0):
			move(North)
		if (swapped == False):
			break