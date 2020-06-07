from django.urls import path
from .views import Where

urlpatterns = [
    path('weather/', Where.as_view(), name='where'),

]