while True:
	c = input("Which course would you like to look up? (Enter x to exit):")
	if c == 'x':
		break
	
	with open("dict", "r") as Dict:
		q = None
		for course in Dict:
			
			Name = course.lower().split()[0:3]
			name = Name[1] + " " + Name[2]
			
			if c.lower().strip() == name.lower().strip():
				q = course
				print(course)
				break
		if q is None:
			print("Unable to find class")