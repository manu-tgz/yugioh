from django.urls import path, re_path
from .views import (DeckGBPlayer, ArchetypeGBPlace, DeckCreateView,
                    PlacePopulateArchetype,ArchetypeGBPlayer)

urlpatterns = [
   #re_path('^purchases/(?P<username>.+)/$', PlayerDeckList.as_view()),
   path('deck/more/', DeckGBPlayer.as_view()),
   path('deck/create/', DeckCreateView.as_view()),
   path('archetypes/popular/', ArchetypeGBPlayer.as_view()),
   path('archetypes/place/', ArchetypeGBPlace.as_view()),
   path('archetypes/popular/place/',PlacePopulateArchetype.as_view()),
]