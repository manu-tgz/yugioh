from django.contrib import admin
from .models import Deck, Card,Archetype

# Register your models here.
admin.site.register(Deck)
admin.site.register(Archetype)