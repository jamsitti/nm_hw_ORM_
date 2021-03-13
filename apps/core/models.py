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

#So far I have gotten the search page to load without adding pokemon data
# to this database.

#Itd be great if I could have a selection from a dropdown that changes when you
# type letters, but how do I get each pokemon name into a database
class SearchInquiry(models.Model):
    pokemon_name = models.CharField(max_length=100)

class InquiryForm(forms.ModelForm):
    class Meta:
        model = SearchInquiry
        fields = ['pokemon_name']

#Need a model for UserTeams
#   put n:1 connection with profiles, even though their can be 1:1. This is bc
#   if a profile gets deleted, their team needs to CASCADE del as well
class UserTeam(models.Model):
    #username = connect this with User profile
    #teamname = let them pick a nameeeeeee
    #pokemon_1 = #make sure its not necessary, add these through search page
    #through a little icon like a catch and a release
    #pokemon_2 = 
    #pokemon_3 = 
    #pokemon_4 = 
    #pokemon_5 = 
    #pokemon_6 = 


#Need a model for TeamPokemon
#   dont forget to put many to one connection, many team pokemon with one team
#   if a team is deleted, the pokemon will not be deleted. Perhaps many to many? 



#Need a form for populating UserTeams with TeamPokemon object


