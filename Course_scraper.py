import requests
from bs4 import BeautifulSoup as bs


mainURL = "https://courses.students.ubc.ca/cs/main?"

def getLinks(url):
	with requests.Session() as r:
		stuff = []
		for link in url:
			#get page
			if link == "":
				continue

			page = r.get(link)

			if(page.status_code > 200):
				print("Sorry, could not open")
				continue #try again
			#read
			s = bs(page.content,"html.parser")

			#get all the links
			inter = s.findAll("div",{"class":"content expand"})
			if(len(inter) < 1):
				continue

			links = s.findAll("div",{"class":"content expand"})[0].table.tbody.findAll('a')

			#insert the links into a list
			for i in range(len(links)):
				u = links[i]["href"].split("?",2)
				stuff.insert(i,mainURL + u[1])

		#return the list of links
		return stuff
def getClass(url):
	with requests.Session() as r:
		all_courses = []
		for link in url:

			if link == "":
				continue

			#get page
			page = r.get(link)

			if(page.status_code > 200):
				print("Sorry, could not open")
				continue #try again
			#read
			s = bs(page.content,"html.parser")

			info = s.findAll("div",{"class":"content expand"})[0].findAll('p')
			title = s.findAll("div",{"class":"content expand"})[0].h4.text.split()

			from functools import reduce

			name = reduce(lambda x,y: x + " " + str(y),title[0:2])

			desciption = info[0].text.strip() 
			creds = info[1].text

			if(len(info) >= 3):
				from functools import reduce
				words = list(word.strip() for word in info[2].text.split())
				if(len(words) >= 1):
					preReqs = reduce(lambda x, y: x + " " + str(y),words)
					desciption += " "+ preReqs

			thisCourse ={"name" : name, "credits": creds, "desciption" : desciption}
			all_courses.append(thisCourse)

		return all_courses


def getDict():
	mainURL = "https://courses.students.ubc.ca/cs/main?"
	mainLink = ["https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=0",""]
	#the dept links
	deptLinks = getLinks(mainLink)
	#the class links
	classLinks = getLinks(deptLinks)
	#this gets the name,credits, and description
	Dict = getClass(classLinks)
	return Dict

    