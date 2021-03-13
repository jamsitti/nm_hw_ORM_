from django.db import models
from django.db.models import fields
from django.forms.widgets import SplitHiddenDateTimeWidget, Textarea
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

#I made this and I'm not sure if I need it!

#What would the right fields be for types??

class Pokemon(models.Model):
    image_src = models.CharField(max_length=127)
    #sprite = models.ImageField()
    #type1 = models.ImageField()
    #type2 = models.ImageField()
    name = models.CharField(max_length=127)
    atk = models.IntegerField()
    defense = models.IntegerField()
    sp_atk = models.IntegerField()
    sp_def = models.IntegerField()
    speed = models.IntegerField()
    hp = models.IntegerField()
    
#Need to specify...........
# User class/models, userTeam models (he called this the dashboard,
# these are n:1 towards Users), teamMember class/models (dashboard panel?, 
# these are n:1 towards userTeam), Pokemon class? Like an abstract class that will
# get certain information on a pokemon if requested

#DASHBOARD PANEL
class TeamDashboardPanel(models.Model):
    account_username = models.CharField(max_length=50)
    team_name = models.CharField(max_length=50)
    panel_type = models.CharField(max_length=127, choices=[
      ("piechart", "Pie-chart of languages used"),
       ("barchart", "Bar-chart of languages used"),
    ])
    team_bio = models.TextField(max_length=140)
    #pokemon_on_team = perhaps a list of the objects from the teamMember class?
    #card = set the style of the card or display for your team

#HOW TO REGISTER DASHBOARD PANEL IN ADMIN.PY
    #import admin
    #from .models import TeamDashboardPanel
    #admin.site.register(TeamDashboardPanel)

#model for search inquiry for a pokemon?
class SearchInquiry(models.Model):
    pokemon_name = models.CharField(max_length=100)

class InquiryForm(forms.ModelForm):
    class Meta:
        model = SearchInquiry
        fields = ['pokemon_name']