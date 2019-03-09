from django.urls import path

import views

# In this example, we've separated out the views.py into a new file
urlpatterns = [
    path('', views.about),
    path('about', views.about),
    path('rules', views.rules),
    path('play', views.play),
    path('character-cards', views.character_cards),
    path('sample-setup', views.under_construction),
    path('gameplay-details', views.gameplay_details),
    path('contact', views.contact),
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
