import requests
from django.http import HttpResponse
from django.shortcuts import render


cards = [{
    'card_title': 'Hacker',
    'card_skill_1': 'Steal: Take 2 coins from another player',
    'card_skill_2': 'Blocks inspection',
    'img_src': '../static/img/hacker.svg'},
    {'card_title': 'Inspector',
        'card_skill_1': 'Inspect: Look at another card, then return it',
        'card_skill_2': 'Blocks stealing',
        'img_src': '../static/img/inspector.svg'},
    {'card_title': 'Athlete',
        'card_skill_1': 'Compete: Take 3 coins from the stash',
        'card_skill_2': 'Blocks other competition',
        'img_src': '../static/img/athlete.svg'},
    {'card_title': 'Hunter',
        'card_skill_1': 'Target: Pay 7 coins to take the gun from the mantle',
        'card_skill_2': 'Skill cannot be replicated',
        'img_src': '../static/img/hunter.svg'},
    {'card_title': 'Scientist',
        'card_skill_1': 'Replicate: Repeat the previous skill used',
        'card_skill_2': 'Blocks exchanges',
        'img_src': '../static/img/scientist.svg'},
    {'card_title': 'Teacher',
        'card_skill_1': 'Exchange: Switch this card with any player',
        'card_skill_2': 'Blocks Targeting by Hunter',
        'img_src': '../static/img/teacher.svg'}]


def about(request):
    context = {}
    return render(request, "about.html", context)


def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/michaelpb/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)


def under_construction(request):

    return HttpResponse('''
        This page is currently being built. Sorry for the inconvenience!
    ''')


def rules(request):
    context = {}
    return render(request, "rules.html", context)


def play(request):
    context = {}
    return render(request, "play.html", context)


def character_cards(request):
    context = {'all_cards': cards}
    return render(request, "character-cards.html", context)


def gameplay_details(request):
    context = {}
    return render(request, "gameplay-details.html", context)


def contact(request):

    return
