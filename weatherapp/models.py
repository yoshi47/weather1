from django.db import models
import requests
from bs4 import BeautifulSoup

# Create your models here.

class WeatherModel(models.Model):
    where = models.CharField(max_length=100)

