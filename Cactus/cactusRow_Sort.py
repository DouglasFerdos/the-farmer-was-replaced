def cactus_rowSort():
	l_m = []
	for i in range(get_world_size()):
		l_m.append(measure())
		move(East)
	s = len(l_m)
	
	for i in range(s):
		swapped = False
		
		for j in range(s-1):
			if (l_m[j] > l_m[j+1]):
				temp = l_m[j]
				l_m[j] = l_m[j+1]
				l_m[j+1] = temp
				swapped = True
				swap(East)
				move(East)
			elif (get_pos_x() < (s-i-1)):
				move(East)
		#goToPos
		g_x = 0
		x = get_pos_x()
		while (g_x != x):
			x = get_pos_x()
			if (x != g_x):
				if (x < g_x):
					move(East)
				else:
					move(West)
	
		while (get_pos_x() != 0):
			move(East)
		if (swapped == False):
			break