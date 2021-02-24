from django.urls import path
import requests

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]

#response = requests.get('https://pokeapi.co/api/')
#data = response.json()
#print(data)
