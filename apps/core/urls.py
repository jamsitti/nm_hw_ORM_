from django.urls import path

from apps.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('graph/', views.graph, name='graph'),
    path('chart/', views.chart, name='chart'),
]