# Generated by Django 3.1.7 on 2021-03-17 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_pokemon_pokemon_sprite_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userteams',
            name='username',
        ),
    ]
