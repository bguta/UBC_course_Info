import requests
from bs4 import BeautifulSoup as bs


mainURL = "https://courses.students.ubc.ca/cs/main?"

def getLinks(url):
	with requests.Session() as r:
		stuff = []
		for link in url:
			#get page
			page = r.get(url)

			 if(page.status_code > 200):
                print("Sorry, could not open")
                continue #try again
            #read
            s = bs(page.content,"html.parser")

            #get all the links
            links = s.findAll("div",{"class":"content expand"})[0].table.tbody.findAll('a')

            #insert the links into a list
            for i in range(len(links)):
				u = links[i]["href"].split("?",2)
				stuff.insert(i,mainURL + u[1])

		#return the list of links
		return stuff
def getClass(url):
	with requests.Session() as r:
	
	stuff = []
	for link in url:
		#get page
		page = r.get(url)

		if(page.status_code > 200):
        	print("Sorry, could not open")
            continue #try again
        #read
        s = bs(page.content,"html.parser")

        info = s.findAll("div",{"class":"content expand"})[0].findAll('p')
        title = s.findAll("div",{"class":"content expand"})[0].h4.text.split()

        from functools import reduce
        name = reduce(lambda x,y: x+str(y),title[0:2])

        desciption = info[0].text
        creds = info[1].text

        thisCourse ={"name" : name, "credits": creds, "desciption" : desciption}
        stuff.append(thisCourse)

    return stuff

    def getDict():
    	mainLink = ["https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=0"]
    	deptLinks = getLinks(mainLink)
    	classLinks = getLinks(deptLinks)
    	Dict = getDict(classLinks)
    	return Dict

    if __name__ == '__main__'
    	getDict()