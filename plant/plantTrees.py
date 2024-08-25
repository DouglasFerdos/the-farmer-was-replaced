def plantTrees():
	x = get_pos_x()
	y = get_pos_y()
	verifiedHarvest()
	if(x % 2 == 0 and y % 2 == 0) or (x % 2 != 0 and y % 2 != 0):
		plant(Entities.Tree)