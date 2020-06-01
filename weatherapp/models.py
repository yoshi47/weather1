import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class TodayWeather(models.Model):
    where = models.CharField(max_length=180)

    def __str__(self):
        return self.where
