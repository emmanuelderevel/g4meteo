from django.shortcuts import render
import requests
import json
from django.http import HttpResponseRedirect
from .forms import NameForm
import Weather

#Afficher les données météo à partir de l'id de la ville
def weather(request, city_id):
    weather1=Weather(city_id)
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?id={0}&units=metric&APPID=4507f11de27d6470f011743a710aed13'.format(city_id))
    data = r.json()
    temperature=data['main']['temp']
    temp=str(temperature)
    return render(request, 'city/weather.html', locals())


#Rechercher l'id d'une ville à partir de son nom
def get_city_id(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            nom_ville=form.cleaned_data['city_name']
            json_data=open('cities.json')
            data = json.load(json_data)
            L=[]
            for i in range(0,len(data)):
                if data[i]['name']==nom_ville:
                    L=L+[data[i]]
            return render(request, 'city/results.html', locals())

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'city/find.html', {'form': form})


