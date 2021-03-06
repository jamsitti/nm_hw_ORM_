from django.db import models
from django.forms.widgets import SplitHiddenDateTimeWidget

#I made this and I'm not sure if I need it!

class Pokemon(models.Model):
    image_src = models.CharField(max_length=127)
    name = models.CharField(max_length=127)
    atk = models.IntegerField()
    defense = models.IntegerField()
    sp_atk = models.IntegerField()
    sp_def = models.IntegerField()
    speed = models.IntegerField()
    hp = models.IntegerField()
    