bool_hay = num_items(Items.Hay) < 80000
bool_wood = num_items(Items.Wood) < 80000
bool_carrot = num_items(Items.Carrot) < 80000
bool_carrot_seeds = num_items(Items.Carrot_Seed) > 0
bool_pumpking = num_items(Items.Pumpkin) < 80000
bool_pumpking_seeds = num_items(Items.Pumpkin_Seed) > 0
bool_sunflower = num_items(Items.Power) < 25000
bool_gol_D = num_items(Items.Gold) < 50000
bool_cactus = num_items(Items.Cactus) < 50000
returnToSpawn()

#while True:
for i in range(get_world_size()):
	for j in range(get_world_size()):
		planting()
		move(North)
	move(East)