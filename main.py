import requests
import bs4

baseUrl = 'https://parkinlyon.fr'
uri = '/tous-les-parkings'

response = requests.get(baseUrl + uri)

if response.ok:
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    div = soup.find('div', {"id" : "request-container"})
    list = div.findAll('div', {"class" : "card ombre h-100"})
    urls = []
    for name in list:
        print('Nom : ' + name.find('h5').contents[0])
        print('URL : ' + baseUrl + name.find('a').attrs['href'])
        urls.append(baseUrl + name.find('a').attrs['href'])

        try:
            print('Places : ' + str(int(name.find('h2').contents[0].replace(' places libres', ''))) + '/' + name.find('p').find('small').contents[0].replace('capacité : ', '').replace(' places', ''))
        except:
            if name.find('h2').contents[0].replace(' places libres', '') == 'INDISPONIBLE':
                print('0/' + name.find('p').find('small').contents[0].replace('capacité : ', '').replace(' places', ''))
            else:
                print('Impossible d\'obtenir le suivi de ce parking !')
        print('\n')
    print(urls)