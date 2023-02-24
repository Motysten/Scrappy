# ensure you have Python (3  or latest)
# ensure you have pip installer

from Scraper import Scraper
from Park import Park

# L'url du site que je souhaite Scraper
baseUrl = 'https://parkinlyon.fr'
uri = "/tous-les-parkings#"

parkInstance = Park(baseUrl, uri, 0)

scraper = Scraper(parkInstance, "linksList.csv", "infos.csv")

scraper.exec()

print("Done")