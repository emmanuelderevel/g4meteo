import requests

class Forecast:
    def __init__(self, nom_ville):
        self.nom_ville=nom_ville
        self.forecast_list=[]

    def retrieve_forecast(self):
        r = requests.get('http://api.openweathermap.org/data/2.5/forecast?q={0}&units=metric&APPID=4507f11de27d6470f011743a710aed13'.format(self.nom_ville))
        data = r.json()
        L=data['list']
        for l in L:
            time=l['dt_txt']
            temperature=l['main']['temp']
            self.forecast_list=self.forecast_list+[(time, temperature)]

if __name__=='__main__':
    f1=Forecast('Paris')
    f1.retrieve_forecast()
    print(f1.forecast_list)
