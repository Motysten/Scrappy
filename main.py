import requests
import bs4

baseUrl = 'https://parkinlyon.fr'
uri = '/tous-les-parkings'

response = requests.get(baseUrl + uri)

if response.ok:
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    div = soup.find('div', {"id" : "request-container"})
    list = div.findAll('h5')
    for name in list:
        print(name.contents[0])