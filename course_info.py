from Course_scraper import getDict

Dict = getDict()

while True:
	wait = input("Which course would you like to look up? (Enter x to exit):")
	if wait == 'x':
		break
	course = None
	for c in Dict:
		if c["name"].lower() == wait.lower():
			course = c

	if(course != None):
		print("")
		print("name: " + course["name"])
		print("credits: " + course["creds"])
		print("desciption " + course["desciption"])
		print("")

	else:
		print("Unable to find class")