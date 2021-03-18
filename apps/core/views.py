from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import requests
from requests import status_codes
from django.contrib import messages
import pygal
from .models import *
from .forms import *


#This function purely handles grabbing the pokemon data from a user input
# when called in the search view function, which connects to the search bar
# on the home page.


#I need to find an efficient way to extract information that can be stored into
# a TeamMember object for profiles to put on their teams.


def get_api_data(form_data):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + form_data + '/')
    pokemon_data = response.json()
    return pokemon_data


def check_database(pokemon_name, pokemon_sprite):
    all_pokemon = Pokemon.objects.filter(pokemon_name=pokemon_name).values()
    already_added = False
    print('the querySet for any objects in database with the same name is', all_pokemon)

    for pokemon in all_pokemon:
        if pokemon_name in pokemon['pokemon_name']:
            already_added = True

    if already_added == False:
        print('Pokemon added to pokemon objects')
        pokemon=Pokemon.objects.create(pokemon_name=pokemon_name, pokemon_sprite_url=pokemon_sprite)
    else:
        print('Pokemon already in database')


#Views functions begin here.


def home(request):
    context = {
    }
    return render(request, 'pages/home.html', context)


def search_page(request):
    #Loads after a pokemon is typed into homepage's searchbar, reads pokemon's
    #data.
    search_term = request.GET['user_response']
    print(search_term)

    pokemon_data = get_api_data(form_data=search_term)

    pokemon_stats = pokemon_data['stats']
    pokemon_name = pokemon_data['name']
    pokemon_img = pokemon_data['sprites']['other']['official-artwork']['front_default']
    pokemon_sprite = pokemon_data['sprites']['front_default'] #?

    check_database(pokemon_name, pokemon_sprite)

    line_chart = pygal.HorizontalBar()
    line_chart.title = pokemon_name.capitalize() + ' stat spread'
    for stat_key in pokemon_stats:
        value = stat_key['base_stat']
        label = stat_key['stat']['name'].capitalize()
        line_chart.add(label, value)
    chart_svg = line_chart.render()

    context = {
        'search_term': search_term,
        'pokemon': pokemon_name.upper(),
        'stats': pokemon_stats,
        "rendered_chart_svg": chart_svg,
        'img': pokemon_img,
        'pokemon_data': pokemon_data,
    }

    return render(request, 'pages/search.html', context)


@login_required
def create_team(request):
    if request.method == 'POST':
        form = CreateTeamForm(request.POST)

        if form.is_valid():
            team = form.save(commit=False)
            team.creator_user = request.user
            team.save()
            messages.success(request, 'Team created successfully. Welcome!')
            return redirect(request.META.get('HTTP_REFERER', '/view_teams/'))
    else:
        form = CreateTeamForm()

    context = {
        'form': form,
    }
    return render(request, 'pages/create_team.html', context)


@login_required
def update_team(request, team_id):
    team_name = request.POST['teamname']
    team_slogan = request.POST['team_slogan']

    # Update the team
    team = UserTeam.objects.get(id=team_id)
    team.teamname = team_name
    team.team_slogan = team_slogan
    team.save()

    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def view_teams(request):
    #Reads all team objects onto teams page.

    #add verification for what page needs to show
    user = request.user.id
    user_has_team = UserTeam.objects.filter(creator_user_id=request.user.id).exists
    if user_has_team == True:
        all_teams = UserTeams.objects.all()
        context = {
            "all_teams": all_teams,
            'user_has_team': user_has_team,
        }

        return render(request, "pages/view_teams.html", context)
    else:
        load_link = True
        context = {
            'load_link': load_link,
        }

        return render(request, "pages/view_teams.html", context)

    #if user.is_authenticated and UserTeams.creator_user != request.user:



#TODO: Need to define poke_id!

@login_required
def add_to_team(request, poke_id):
    pokemon = Pokemon.objects.get(id=poke_id)
    userTeam = UserTeam.objects.get(user=request.user)

    if len(userTeam) < 6: #??????
        pokemon.liked.add(request.userTeam)
        user.team.save()
        messages.success(request, 'Pokemon added to team!')
    else:
        messages.MessageFailure(request, 'You already have a full team')

    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def remove_from_team(request, poke_id):
    team_pokemon = Pokemon.objects.get(id=poke_id)

    # BONUS: Security
    if team_pokemon.creator_user == request.user:
        team_pokemon.delete()

    return redirect(request.META.get('HTTP_REFERER', '/'))




#Before I had view functions that make prespecified static pages, now id like to
# have one page for viewing a pokemons data and have the focus be on userTeam. user
# and user team have to be different models, and I also need models possibly for each
# pokemon? Or at least a model that pulls data from the API when a requests asks to
# show data on a specific pokemon. 

#Overall all of the pages that we need are...............
# 1) homepage that show three random profiles and also links to the pokesearch 
# page and all users page, [READ]
# 2) a pokesearch page that will either ask to pick a pokemon from a dropdown 
# bar or a fill in text field OR [READ]
# it will show the data of the specific pokemon if redirected to that page [perhaps
# this should be two pages], [READ]
# 3) a page that shows a user profile, if it is the logged in persons profile then 
# they will have the option to modify their team aka adding or removing pokemon and
# also of modifying profile like name and username email etc.[READ / UPDATE / DELETE]
# 4) a login page and a sign up page (sign up can either be on the front or be
# connected to the log in page) [CREATE / LOGIN-READ ]
# 5) a page that shows a certain amount of the users and their team on a widget
# perhaps about like 15 users? [READ]


#Have to make all of this accesible through the admin page?? Like gorl idk bout dat

#ALSO YOU GON HAVE TO UPDATE THE CSS AND MAKE THAT ISH CUTE, ALSO YOU GON HAVE TO
# CHANGE AND MAKE LIKE A ZILLION WEBPAGES BUT TBH UR GONNA BE FINE
# THAT API IS GONNA BE UR BIGGEST STRUGGLE BUT I BELIEVE IN U



#HOW TO LIST INSTANCES IN A VIEW
#Clue 2: Listing instances in a view

    #1. Use it in a view. For example:


    #2. Reference it in a template. For example:
    #{% for panel in dboard_panels %}
            #<div class="shadow border"> <!-- Example HTML / CSS -->
            #<p>{{ panel.title }}</p>
    #   <a href="/details/{{ panel.id }}/">Click for more</a>
    #   </div>
    #{% endfor %}