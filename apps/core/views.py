from django.shortcuts import render
import requests
from requests import status_codes
import pokepy
import pygal


#This section develops the data that will be placed throughout multiple view functions
#and templates.
response = requests.get('https://pokeapi.co/api/v2/pokemon/breloom/')
breloom_data = response.json()
breloom_stats = breloom_data['stats']
breloom_name = breloom_data['name']
breloom_sprite = breloom_data['sprites']['other']['official-artwork']['front_default']

#These views functions send data to the html templates. The home page is used for 
#navigation.
def home(request):
    context = {
    }
    return render(request, 'pages/home.html', context)


def graph(request):
    context = {
        'pokemon': pokepy.V2Client().get_pokemon('breloom'),
        'stats': breloom_stats,
    }
    return render(request, 'pages/graph.html', context)


def chart(request):


    #stat_list = []
    #for i in range(6):
    #    stat_list += breloom_stats['stats'][str(i)]['name']

    #stats_chart = pygal.Pie()
    #stats_chart.title = "Breloom's stat spread (in %)"
    #for repo_dict in repo_list:
    #    value = 42 # TODO: Replace this...
    #    label = repo_dict["name"]
    #    chart.add(label, value)

    #chart_svg = stats_chart.render()

    context = {
        'pokemon': breloom_name.upper(),
        'stats': breloom_stats,
        "rendered_chart_svg": chart_svg,
        'sprite': breloom_sprite,
    }
    return render(request, 'pages/chart.html', context)
