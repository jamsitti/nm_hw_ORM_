from django.urls import path

from apps.core import views

#you gon need lots of urls

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_page, name='search'),
    #homepanels needs to be user teams
    path('home_panels/', views.view_panels, name='view_panels'),
]