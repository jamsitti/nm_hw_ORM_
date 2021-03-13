#from django.contrib.auth.models import User
from apps.accounts.models import User
from django.db import models
from django.db.models import fields
from django.db.models.fields.files import ImageField
from django.forms.widgets import SplitHiddenDateTimeWidget, Textarea
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


#Need to specify...........
# User class/models, userTeam models (he called this the dashboard,
# these are n:1 towards Users), teamMember class/models (dashboard panel?, 
# these are n:1 towards userTeam)

class Pokemon(models.Model):
    pokemon_name = models.CharField(max_length=100)
    #pokemon_sprite = models.ImageField()


#Need a model for UserTeams
#   put n:1 connection with profiles, even though their can be 1:1. This is bc
#   if a profile gets deleted, their team needs to CASCADE del as well

class UserTeams(models.Model):
    username = models.CharField(max_length=100)
    teamname = models.CharField(max_length=100)
    team_slogan = models.CharField(max_length=150)
    #pokemon_1 = #make sure its not necessary, add these through search page
    #through a little icon like a catch and a release
    #pokemon_2 = 
    #pokemon_3 = 
    #pokemon_4 = 
    #pokemon_5 = 
    #pokemon_6 =
    #panel_type = models.CharField(max_length=127, choices=[
    #  ("piechart", "Pie-chart of languages used"),
    #   ("barchart", "Bar-chart of languages used"),
    #])
    creator_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    #How can I make it so you only can have six?
    liked = models.ManyToManyField(
        Pokemon,
        related_name="pokemon_on_team",
    )