def plantHay():
	verifiedHarvest()
	if get_ground_type() != Grounds.Turf:
		till()