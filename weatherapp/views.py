from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import WeatherModel

# Create your views here.

class Where(CreateView):
    template_name = 'where.html'
    model = WeatherModel
    fields = ('where',)
    success_url = reverse_lazy('result')