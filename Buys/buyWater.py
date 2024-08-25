def buyWater():
	if num_items(Items.Water_Tank) < 10:
		trade(Items.Empty_Tank,10)