def tillIfNeeded():
	if get_ground_type() != Grounds.Soil:
		till()