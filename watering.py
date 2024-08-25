def watering():
	buyWater()
	if (get_entity_type() != Entities.Grass or get_ground_type() == Grounds.Soil):
		if get_water() < 0.75:
			use_item(Items.Water_Tank)