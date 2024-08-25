def harvestCacti():
	if(num_items(Items.Cactus) < (50000)):
		returnToSpawn()
		for i in range(get_world_size()):
			cactus_rowSort()
			move(North)
			
		returnToSpawn()
		for j in range(get_world_size()):
			cactus_columnSort()
			move(East)
		returnToSpawn()
		harvest()