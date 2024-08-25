def verifiedHarvest():
	if get_entity_type() != Entities.Pumpkin:
		if can_harvest():
			harvest()