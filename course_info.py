while True:
	c = input("Which course would you like to look up? (Enter x to exit):")
	if c == 'x':
		break
	
	with open("dict", "r") as Dict:
		found = None
		for course in Dict:
			
			Name = course.lower().split()[0:3]
			name = Name[1] + " " + Name[2]
			
			if c.lower().strip() == name.lower().strip():
				found = course
				print()
				print(course)
				break
			
		if found is None:
			print("Unable to find class")