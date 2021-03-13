from django.urls import path

from apps.core import views

#you gon need lots of urls

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_page, name='search'),
    path('view_teams/', views.view_teams, name='view_teams'),
]