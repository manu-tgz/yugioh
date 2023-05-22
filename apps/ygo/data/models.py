from django.db import models
from apps.users.data.models import Player


class Archetype(models.Model):
    name = models.CharField(primary_key=True, max_length = 50)

    class Meta:
        verbose_name = "Archetype"
        verbose_name_plural = "Archetypes"

    def __str__(self):
        return self.name

class CardManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()

class Card(models.Model):
    """Model definition for Card."""
    class Type(models.TextChoices):
        MONSTER = "Monster"
        TRAMPA = 'Trampa'
    
    name = models.CharField(max_length = 30)
    class_type = models.CharField(max_length = 20, choices=Type.choices)
    archetype = models.ForeignKey(Archetype, verbose_name="archetype",
                                  on_delete=models.CASCADE)
    
    # objects = CardManager()
 
    class Meta:
        """Meta definition for Card."""
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

    def __str__(self):
        """Unicode representation of Card."""
        pass

class DeckManager(models.Manager):
    # TODO: Implementar get cartas  Hint: recorrer Deck_Cards
    # TODO: Implemtar post cartas (Update)
    # TODO: Quien hacer el permiso de editar deck
    def get_queryset(self):
        return super().get_queryset().filter()


class Deck(models.Model):

    """Model definition for Deck."""
    name = models.CharField(max_length=50, verbose_name="name")
    player = models.ForeignKey(Player,null = True, verbose_name="player", on_delete=models.CASCADE)
    main_deck = models.PositiveSmallIntegerField()
    extra_deck = models.PositiveSmallIntegerField()
    side_deck = models.PositiveSmallIntegerField()
    archetype = models.ForeignKey(Archetype, verbose_name="archetype", related_name="decks",
                                  on_delete=models.CASCADE) 
       
    # objects = DeckManager()
    class Meta:
        """Meta definition for Deck."""
        
class DeckCards(models.Model):
    """Model definition for DeckCards."""
    card = models.ForeignKey(Card, verbose_name="card", on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, verbose_name="deck",related_name="cards", on_delete=models.CASCADE)
    MD = models.BooleanField()
    SD = models.BooleanField()
    ED = models.BooleanField()
    
    class Meta:
        """Meta definition for DeckCards."""

        verbose_name = 'DeckCards'
        verbose_name_plural = 'DeckCardss'

    def __str__(self):
        """Unicode representation of DeckCards."""
        pass



   