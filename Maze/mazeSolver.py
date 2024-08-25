def maze():
	#Creates the maze
	if (get_entity_type() != Entities.Hedge):
		plant(Entities.Bush)
		
	while get_entity_type() == Entities.Bush:
		if num_items(Items.Fertilizer) < 100:
			trade(Items.Fertilizer, 100)
		while(get_entity_type() != Entities.Hedge):
			use_item(Items.Fertilizer)

	#Variables
	l_xy, l_xy_n, l_xy_s, l_xy_e, l_xy_w = [],[],[],[],[]
	l_pmoves, l_visited = [],[]

	while (get_entity_type() == Entities.Hedge and num_items(Items.Gold) < 50000):
		#Variables
		l_xy = [get_pos_x(),get_pos_y()]
		l_xy_n = [get_pos_x(),get_pos_y()+1]
		l_xy_s = [get_pos_x(),get_pos_y()-1]
		l_xy_e = [get_pos_x()+1,get_pos_y()]
		l_xy_w = [get_pos_x()-1,get_pos_y()]

		if l_xy not in l_pmoves:
			l_pmoves.append(l_xy)
		if l_xy_n not in l_pmoves and l_xy_n not in l_visited and move(North):
			l_xy = [get_pos_x(),get_pos_y()]
			l_pmoves.append(l_xy)
		elif l_xy_e not in l_pmoves and l_xy_e not in l_visited and move(East):
			l_xy = [get_pos_x(),get_pos_y()]
			l_pmoves.append(l_xy)
		elif l_xy_s not in l_pmoves and l_xy_s not in l_visited and move(South):
			l_xy = [get_pos_x(),get_pos_y()]
			l_pmoves.append(l_xy)
		elif l_xy_w not in l_pmoves and l_xy_w not in l_visited and move(West):
			l_xy = [get_pos_x(),get_pos_y()]
			l_pmoves.append(l_xy)
		else:
			if l_xy in l_pmoves:
				index = len(l_pmoves)-1
				l_xy_last = l_pmoves[index]
				if l_xy == l_xy_last:
					l_xy = [get_pos_x(),get_pos_y()]
					l_visited.append(l_xy)
					index -= 1
					l_xy_new = l_pmoves[index]
					g_x = l_xy_new[0]
					g_y = l_xy_new[1]
					l_pmoves.pop()
					#Start Move To
					x,y = get_pos_x(), get_pos_y()
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
					#End Move To
	if (get_entity_type() == Entities.Treasure):
		harvest()