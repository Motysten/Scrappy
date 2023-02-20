import requests
import bs4
import csv

baseUrl = 'https://parkinlyon.fr'
uri = '/tous-les-parkings'

response = requests.get(baseUrl + uri)

if response.ok:
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    div = soup.find('div', {"id" : "request-container"})
    list = div.findAll('div', {"class" : "card ombre h-100"})
    urls = []
    parks = []
    for name in list:
        infos = {}

        print('Nom : ' + name.find('h5').contents[0])
        # infos.append(name.find('h5').contents[0])
        infos["Nom"] = name.find('h5').contents[0]

        print('URL : ' + baseUrl + name.find('a').attrs['href'])
        # infos.append(baseUrl + name.find('a').attrs['href'])
        infos["Lien"] = baseUrl + name.find('a').attrs['href']
        
        urls.append(baseUrl + name.find('a').attrs['href'])

        try:
            print('Places : ' + str(int(name.find('h2').contents[0].replace(' places libres', ''))) + '/' + name.find('p').find('small').contents[0].replace('capacité : ', '').replace(' places', ''))
            # infos.append(str(int(name.find('h2').contents[0].replace(' places libres', ''))) + '/' + name.find('p').find('small').contents[0].replace('capacité : ', '').replace(' places', ''))
            infos["Places"] = str(int(name.find('h2').contents[0].replace(' places libres', ''))) + '/' + name.find('p').find('small').contents[0].replace('capacité : ', '').replace(' places', '')
        except:
            if name.find('h2').contents[0].replace(' places libres', '') == 'INDISPONIBLE':
                print('Places : 0/' + name.find('p').find('small').contents[0].replace('capacité : ', '').replace(' places', ''))
                # infos.append('0/' + name.find('p').find('small').contents[0].replace('capacité : ', '').replace(' places', ''))
                infos['Places'] = '0/' + name.find('p').find('small').contents[0].replace('capacité : ', '').replace(' places', '')
            else:
                print('Impossible d\'obtenir le suivi de ce parking !')
                # infos.append("Error !")
                infos['Places'] = "Error !"
        print('\n')

        parks.append(infos)
    print(urls)

    headers = ["Nom", "Lien", "Places"]

    with open("result.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(parks)