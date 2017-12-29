from Course_scraper import getDict

Dict = getDict()

def make():
	with open("dict",w) as file:
		for course in Dict:
			file.write("name: "+ course["name"].strip() + " credits: " + course["creds"].strip() + " desciption: " + course["desciption"].strip())
