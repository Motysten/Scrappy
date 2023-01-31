import requests
import bs4

baseUrl = 'https://parkinlyon.fr'
uri = '/tous-les-parkings'

response = requests.get(baseUrl + uri)

if response.ok:
    print(response.status_code)