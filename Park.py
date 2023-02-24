from Toolkit import Toolkit
from ParkEntry import ParkEntry
class Park:
    def __init__(self, baseUrl, uri, nbPage):
        self.baseUrl = baseUrl
        self.uri = uri
        self.setPageMax(nbPage)
        self.urls = []
        self.endpoints = []
        self.result = []
        self.finalFileNameFields = ["name","address","capacity", "left", "owner", "link"]

    def setPageMax(self, pageMax):
        self.nbPage = pageMax + 1
        return self
    
    def getLinks(self):
        for i in range(self.nbPage):
            self.urls.append(self.baseUrl + self.uri + str(i))
        return self.urls
    
    def setEndpoints(self, soup):
        container = soup.find("div", {"id" : "request-container"})
        divs = container.findAll("div", {"class" : "col-lg-4 col-md-6 my-2"})
        links = []
        for div in divs:
            a = div.find("a")
            try:
                links.append(a["href"])
            except:
                pass
        self.endpoints.extend(Toolkit.addBaseUrl(self.baseUrl, links))
        return self.endpoints

    def getEndpoints(self):
        return self.endpoints

    def getFinalFieldNames(self):
        return self.finalFileNameFields
    
    def getInfoByPage(self, soup):
        fiches = []
        name = Toolkit.tryToCleanOrReturnBlank(soup.find("h1", {"class" : "name"}))
        address = Toolkit.tryToCleanOrReturnBlank(soup.find("div", {"class" : "card-block"}).find("p", {"class" : "text-center"}))
        capacity = Toolkit.tryToCleanOrReturnBlank(soup.find("div", {"class" : "card-block"}).find("p")).replace("capacité : ", "").replace(" places", "")
        left = Toolkit.tryToCleanOrReturnBlank(soup.find("div", {"class" : "card-block"}).find("h2")).replace(" places libres", "").replace("INDISPONIBLE", "0")
        owner = Toolkit.tryToCleanOrReturnBlank(soup.findAll("div", {"class" : "col-lg-6 col-md-6 col-sm-12"})[2].find("p")).replace("Gestionnaire du parking : ", "")
        divs = soup.findAll("div", {"class" : "col-lg-6 col-md-6 col-sm-12"})
        if len(divs) == 4:
            link = divs[3].find("a")['href']
        else:
            link = "https://portfolio.motysten.fr"
        
        print("Les infos de " + name + " ont bien été scrapées !")
        fiche = ParkEntry(name, address, capacity, left, owner, link)
        fiches.append(fiche)
        self.result.extend(fiches)
        return fiches
    
    def getResult(self):
        return self.result

    def getDictResult(self):
        result = []
        for res in self.getResult():
            result.append(res.getDictEntry())
        return result