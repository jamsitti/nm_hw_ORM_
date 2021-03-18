from django.urls import path

from apps.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_page, name='search'),
    path('view_teams/', views.view_teams, name='view_teams'),
    path('view_teams/create_team/', views.create_team, name='create_team'),
    path('add_to_team/', views.add_to_team, name='add_to_team'),
    path('remove_from_team/', views.remove_from_team, name='remove_from_team'),
]