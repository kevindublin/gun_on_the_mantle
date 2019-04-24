import requests
import utils
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

cards = utils.write_cards()


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


def example_scenario(request):
    context = {}
    return render(request, "example-scenario.html", context)


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


def send_email(request):
    print("sending contact form e-mail...")
    send_mail(
        subject=request.POST["name"]+" - About Gun on the Mantle",
        message=request.POST["message"],
        from_email=request.POST["email"],
        recipient_list=['admin@kevindublin.com'],
        fail_silently=True,
        )
    print('sent.')
    context = {
        'email_sent': 'True',
        'message': 'Your e-mail was successfully sent!',
    }
    return render(request, "about.html", context)


def sample_setup(request):
    context = {}
    return render(request, "sample-setup.html", context)
