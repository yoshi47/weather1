from django.urls import path

from .views import Weatherapp, index

urlpatterns = [
    path('', index, name='index'),
    path('weather/', Weatherapp.as_view(), name='weather')
]
