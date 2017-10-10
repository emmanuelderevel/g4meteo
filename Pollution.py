import requests
import re

class Pollution():

    def __init__(self,dict,lon,lat,dtime):
        self.dict={}
        self.lon=lon
        self.lat=lat
        self.dtime=dtime

    def retrivePollInfo(self):
        html = 'http://api.openweathermap.org/data/2.5/uvi?' \
               'lat={}&lon={}&appid=955716c6c3b27005023580d9021147ba'.format(self.lat,self.lon)
        client = requests.get(html)
        j = client.json()
        self.dict = j['value']

    def __str__(self):


