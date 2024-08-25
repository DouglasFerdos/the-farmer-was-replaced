def returnToSpawn():
	g_x = 0
	g_y = 0
	x = get_pos_x()
	y = get_pos_y()
	while (g_x != x or g_y != y):
		x = get_pos_x()
		y = get_pos_y()
		if (x != g_x):
			if (x < g_x):
				move(East)
			else:
				move(West)
		if (y != g_y):
			if (y < g_y):
				move(North)
			else:
				move(South)