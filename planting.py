def planting():
	if bool_sunflower:
		buySunflowersSeeds()
		plantSunflowers()
	elif bool_hay:
		plantHay()
	elif bool_wood:
		plantTrees()
	elif bool_carrot:
		buyCarrotSeeds()
		plantCarrot()
	elif bool_pumpking:
		buyPumpkingSeeds()
		plantPumpking()
	elif bool_gol_D:
		maze()
	elif bool_cactus:
		buyCactusSeeds()
		plantCactus()
		harvestCacti()