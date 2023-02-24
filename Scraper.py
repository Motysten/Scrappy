import requests 
from bs4 import BeautifulSoup 
from Toolkit import Toolkit
class Scraper:
    def __init__(self, ScrapInstance, linkFile, finalFile):
        self.setScrapInstance(ScrapInstance)
        self.setFinalFile(finalFile)
        self.setLinkFile(linkFile)
        self.finalFileNameFields = self.ScrapInstance.getFinalFieldNames()
        self.linkFileNameFields = ['id', 'link']

    def setScrapInstance(self, instance):
        self.ScrapInstance = instance
        return self

    def setLinkFile(self, filePath):
        self.linkFile = filePath
        return self

    def setFinalFile(self, filePath):
        self.finalFile = filePath
        return self

    def swoup(self, url, process):
        #Instanciation de mon proxy
        response = requests.get(url)
        #si mon site renvoie un code HTTP 200 (OK)
        if response.ok:
            #je passe le contenue html de ma page dans un "parser"
            soup = BeautifulSoup(response.text, 'html.parser')
            try:
                #Je retourne l'execution de ma fonction process prenan ma SWOUP SWOUP en parametre
                return process(soup)
            except Exception as e:
                print("ERROR: Impossible to process ! On :" + str(url))
                print(e)
                return False

        else:
            print("ERROR: Failed Connect on :" + str(url))
            return False
        return

    def swoupMultiple(self, urls, process):
        result = []
        for url in urls:
            soup = self.swoup(url, process)
            if hasattr(soup, '__len__'):
                result.extend(soup)
            else: 
                result.append(soup)
        return result

    def exec(self):
        self.swoupMultiple(self.ScrapInstance.getLinks(), self.ScrapInstance.setEndpoints)

        i = 0
        rows= []
        for url in self.ScrapInstance.getEndpoints():
            row = {}
            row["link"] = url
            row['id'] = i
            i += 1
            rows.append(row)
        Toolkit.fileWriter(self.linkFile, self.linkFileNameFields, rows)

        self.swoupMultiple(self.ScrapInstance.getEndpoints(), self.ScrapInstance.getInfoByPage)
        Toolkit.fileWriter(self.finalFile, self.finalFileNameFields, self.ScrapInstance.getDictResult() )
