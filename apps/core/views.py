from django.shortcuts import render
import requests
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
    pie_chart = pygal.Pie()
    pie_chart.title = '''Breloom's stat spread (in %)'''
    pie_chart.add('IE', 19.5)
    pie_chart.add('Firefox', 36.6)
    pie_chart.add('Chrome', 36.3)
    pie_chart.add('Safari', 4.5)
    pie_chart.add('Opera', 2.3)
    pie_chart.render()

    chart = pygal.Pie()
    for repo_dict in repo_list:
        value = 42 # TODO: Replace this...
        label = repo_dict["name"]
        chart.add(label, value)

    chart_svg = chart.render()
    context = {
        "rendered_chart_svg": chart_svg,
    }

    context = {
        'pokemon': pokepy.V2Client().get_pokemon('breloom'),
        'stats': breloom_stats,
    }
    return render(request, 'pages/chart.html', context)
