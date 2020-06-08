from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
import requests
from bs4 import BeautifulSoup

from .models import WeatherModel

# Create your views here.

RES_WHERE = requests.get("http://weather.livedoor.com/forecast/rss/primary_area.xml")
URL_WEATHER = "http://weather.livedoor.com/forecast/webservice/json/v1?"

class Where(CreateView):
    template_name = 'where.html'
    model = WeatherModel
    fields = ('where',)
    success_url = reverse_lazy('result')

def result (request):
    point = WeatherModel.objects.get()
    soup = BeautifulSoup(RES_WHERE.text, 'lxml')
    city = soup.find('city', attrs={'title': point})
    city_id = city['id']
    params = {'city': city_id}
    data = requests.get(URL_WEATHER, params=params).json()

