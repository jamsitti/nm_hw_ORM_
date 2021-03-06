from django.urls import path
import requests

from apps.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('graph/', views.graph, name='graph'),
    path('chart/', views.chart, name='chart'),
]

#response = requests.get('https://pokeapi.co/api/')
#data = response.json()
#print(data)

#https://pokeapi.co/api/v2/pokemon/{id or name}/
#METHODS = stats, types, sprites, names

