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
    line_chart = pygal.HorizontalBar()
    line_chart.title = 'Breloom stat spread'
    for stat_key in breloom_stats:
        value = stat_key['base_stat']
        label = stat_key['stat']['name']
        line_chart.add(label, value)

    chart_svg = line_chart.render()

    context = {
        'pokemon': breloom_name.upper(),
        'stats': breloom_stats,
        "rendered_chart_svg": chart_svg,
        'sprite': breloom_sprite,
    }
    return render(request, 'pages/graph.html', context)


def chart(request):
    stats_chart = pygal.Pie()
    stats_chart.title = "Breloom stat spread (in %)"
    for stat_key in breloom_stats:
        value = stat_key['base_stat']
        label = stat_key['stat']['name']
        stats_chart.add(label, value)

    chart_svg = stats_chart.render()

    context = {
        'pokemon': breloom_name.upper(),
        'stats': breloom_stats,
        "rendered_chart_svg": chart_svg,
        'sprite': breloom_sprite,
    }
    return render(request, 'pages/chart.html', context)
