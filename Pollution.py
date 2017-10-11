import requests
import datetime

class Pollution():

    def __init__(self,lon,lat):
        self.value=''
        self.lon=lon
        self.lat=lat

    def retrivePollInfo(self):
        html = 'http://api.openweathermap.org/pollution/v1/co/' \
               '{},{}/{}.json?appid=955716c6c3b27005023580d9021147ba'.format(self.lat,self.lon,datetime.datetime.now)
        client = requests.get(html)
        j = client.json()
        self.value = j['data'][0]['value']


if __name__ == '__main__':
    p=Pollution(51.51,-0.13)
    p.retrivePollInfo()
    print(p.value)