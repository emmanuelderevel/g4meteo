import requests
import re


class Weather():
    def __init__(self, name, country):
        self.dict = {}
        self.country=country
        self.name=name
        self.lon=''
        self.lat=''

    def retriveWeathInfo(self):
        html = 'http://api.openweathermap.org/data/2.5/weather?' \
               'q={},{}&units=metric&APPID=955716c6c3b27005023580d9021147ba'.format(self.name,self.country)
        client = requests.get(html)
        j = client.json()
        self.dict['temp'] = j['main']['temp']
        self.dict['main'] = j['weather'][0]['main']
        self.dict['description'] = j['weather'][0]['description']
        self.dict['humidity'] = j['main']['humidity']
        self.dict['pressure'] = j['main']['pressure']
        self.dict['wind'] = j['wind']['speed']
        self.lon = j['coord']['lon']
        self.lat = j['coord']['lat']
        #self.dtime = j

    def __str__(self):
        return 'Informations météorologiques de la ville de Londre : {}'.format(self.dict)


if __name__ == '__main__':
    p=Weather('London','uk')
    p.retriveWeathInfo()
    print(p.dict)

