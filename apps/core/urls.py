from django.urls import path

from apps.core import views

#goooooorl you gon need lots of urls

urlpatterns = [
    path('', views.home, name='home'),
#    path('graph/', views.graph, name='graph'),
#    path('chart/', views.chart, name='chart'),
    path('search/', views.search_page, name='search'),
    path('home_panels/', views.view_panels, name='view_panels'),
]