from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, ListView

from .models import TodayWeather

# Create your views here.

def index(request):
    return HttpResponse('Hello!')

class Weatherapp(CreateView):
    template_name = 'weather.html'
    model = TodayWeather
    fields = ('where', )

class Today(ListView):
    template_name = 'today.html'
    model = TodayWeather
