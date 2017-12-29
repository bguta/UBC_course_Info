from course_scraper import getDict

print("starting...")
Dict = getDict()

def make():
	with open("dict","w", encoding='utf-8') as file:
		for course in Dict:
			file.write("Name: "+ str(course["name"]).strip() + " " + str(course["credits"]).strip() + " Desciption: " + str(course["desciption"]).strip() + "\n")

make()
print("DONE")
input()