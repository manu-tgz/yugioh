from django.db import models
from django.db.models import Count

from apps.users.data.models import Player, Manager
from apps.ygo.data.models import Deck

class Date(models.Model):
    """Model definition for Date."""
    date = models.DateField(primary_key=True, auto_now=False, auto_now_add=False)

    class Meta:
        """Meta definition for Date."""
        verbose_name = 'Date'
        verbose_name_plural = 'Dates'

class Tournament(models.Model):
    name = models.CharField(max_length=40)
    managers = models.ManyToManyField(Manager,related_name= "tournaments", verbose_name="managers")
    champion = models.ForeignKey(Player,on_delete=models.CASCADE,null = True, related_name = "win_tournaments")                                   
    start_date = models.DateField( auto_now=False, auto_now_add=False) 
    finish_date = models.DateField( auto_now=False, auto_now_add=False, null = True) 
    address = models.CharField(max_length=80)   
    
    def addPlayer(self,_player : Player,_deck: Deck):
        _deck.player = _player
        _deck.save()
        Participant.objects.create(player = _player, deck = _deck, tournament = self)
    
    def players (self):
        return Participant.objects.filter(tournament = self)
    
    def ChampionDeck(self):
        #if self.champion == NULL : return NULL
        participant = Participant.objects.get(player = self.champion)
        return participant.deck
    
    def setChampion(self,player):
        self.champion = player
        self.deckChampion = self.ChampionDeck()
        self.save()
    
    def getChampion(self):
        '''Consulta No_4: El campeón de un torneo. '''
        return self.champion

    def __str__(self):
        return self.name

class Participant(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, related_name= "participants", on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    registration_date = models.ForeignKey(Date, verbose_name="registration", on_delete=models.CASCADE)
      
    # def matchs(self):
    #     Match.objects.filter(player1 = self).filter(player2 = self)

    def __str__(self):
        return  str(self.player) + " | " +str(self.tournament)
    

class Round (models.Model):
    name =  models.CharField(max_length=40)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name= "rounds")
    
    def Matchs(self):
        return Match.objects.filter(round = self)
    def Players(self):
        matchs = self.Matchs()
        return (Participant.objects.filter(matchs1__in = matchs)|Participant.objects.filter(matchs2__in = matchs)).distinct()
    def Decks (self):
        players = self.Players()
        return Deck.objects.filter(id__in = players.values('deck'))
    
    def Arquetipos(self):
        '''Consulta No_9: Dado un torneo y una ronda, cuál o cuáles son los arquetipos 
        más representados (cantidad de jugadores usándolos)'''
        
        decks = self.Decks()
        return decks.values('arquetipo').annotate(count=Count('arquetipo')).order_by('-count')

    def __str__(self):
        return self.name

class Match(models.Model):  
    player1 = models.ForeignKey(Participant, related_name= "matchs1",on_delete=models.CASCADE)
    player2 = models.ForeignKey(Participant, related_name= "matchs2",on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name= "matchs")
    winner = models.ForeignKey(Participant, on_delete=models.CASCADE,null = True, related_name= "win_matchs")
    date = models.ForeignKey(Date, verbose_name="date", on_delete=models.CASCADE)
    result = models.CharField(max_length=4)
    
    def __str__(self):
        return  str(self.player1) +" vs "+str(self.player2)+ "| fecha"



