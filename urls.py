from django.urls import path

import views

# In this example, we've separated out the views.py into a new file
urlpatterns = [
    path('', views.about),
    path('about', views.about),
    path('rules', views.rules),
    path('play', views.play),
    path('character-cards', views.character_cards),
    path('gameplay-details', views.gameplay_details),
    path('example-challenge', views.example_challenge),
    path('example-endgame', views.example_endgame),
    path('send-email', views.send_email),
    path('sample-setup', views.sample_setup),
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
