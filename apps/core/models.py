#from django.contrib.auth.models import User
from apps.accounts.models import User
from django.db import models
from django.db.models import fields
from django.db.models.fields.files import ImageField
from django.forms.widgets import SplitHiddenDateTimeWidget, Textarea
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.apps import apps


class Pokemon(models.Model):
    pokemon_name = models.CharField(max_length=100)
    pokemon_sprite_url = models.URLField(max_length=250, default='https://cdn.bulbagarden.net/upload/9/98/Missingno_RB.png')


class UserTeam(models.Model):
    creator_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    #username = creator_user
    on_team = models.ManyToManyField(
        Pokemon,
        related_name="assigned_team",
    )

    teamname = models.CharField(max_length=100)
    team_slogan = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    #panel_type = models.CharField(max_length=127, choices=[
    #  ("piechart", "Pie-chart of languages used"),
    #   ("barchart", "Bar-chart of languages used"),
    #])

    #How can I make it so you only can have six?

    #ANSWER if statement on webpage