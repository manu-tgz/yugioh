import datetime
from django.db.models import Count, F
from ..data.models import Tournament, Participant, Date, Match,Round
from apps.users.domain.queries import PlayerQueries, ManagerQueries
from apps.users.data.models import Player
from apps.ygo.data.models import Deck
from apps.ygo.domain.queries import DeckQueries
from apps.abstract.domain.queries import AbstractQueries
from django.core.exceptions import ObjectDoesNotExist
from django.db import OperationalError
from apps.abstract.util import string_to_date


class TournamentQueries(AbstractQueries):
    instance=Tournament
    
    def add_managers(tournament, managers):
        for i in managers:
            tournament.managers.add(managers_id = i)            
    
    def register_players(self, tournament_id, players_info):
        
        for player_dic in players_info:
            player = PlayerQueries().get(player_dic['player_id'])
            tournament= self.get(tournament_id)
            deck = DeckQueries.get_deck(player_dic['deck_id'])
            registration_date =self.get_or_create_date(datetime.datetime.strptime(player_dic['registration_date'],
                                                                         '%d/%m/%Y').date())
            
            # if(registration_date < tournament.start_date):                                                
            ParticipantQueries().create( tournament, player, deck, registration_date)
            # else: print("nose puede")
                                
    def get_tournament_start_date(self,tournament):
        date = Tournament.objects.values('start_date').get(id=tournament)
        return date    
    
    def create(self, name, manager, address, start_date, finish_date = None):
        date = string_to_date(start_date)
        d = Tournament.objects.create(name=name, address=address, start_date= date, 
                                      finish_date=finish_date)        
        d.managers.add(ManagerQueries().get(manager))      
    
    def get_or_create_date(self, date):
        dt, created = Date.objects.get_or_create(date = date)
        return dt
    
    def get_participants(tournament):
        return tournament.participants.all()
    
    def champion(tournament_id):
        tournament = TournamentQueries().get(tournament_id)
        return tournament.champion
    
    def tournaments_by_range(start_date, end_date):
        tournaments = Tournament.objects.filter(start_date__range=[start_date, end_date])
        return tournaments
    
    def more_victories(start_date, end_date):
        tournaments = TournamentQueries.tournaments_by_range(string_to_date(start_date), string_to_date(end_date))
        players =  Player.objects.filter(user_id__in = Participant.objects.filter(
            tournament__in = tournaments).values('player').all())
        return players.values('user_id').annotate(wins_tournaments = Count('win_tournaments')).order_by('-wins_tournaments')
        
    def archetype_more_used(tournament_id):
        tournament = TournamentQueries().get(tournament_id)
        players_deck1 =Match.objects.filter(round__tournament = tournament).values('player1__deck')
        players_deck2 =Match.objects.filter(round__tournament = tournament).values('player2__deck')
        decks = (Deck.objects.filter(id__in =players_deck1) | Deck.objects.filter(id__in =players_deck2))
        return decks.values('archetype').annotate(count = Count('archetype')).order_by('-count')
    
    def champions_archetypes(start_date, end_date):
        tournaments = TournamentQueries.tournaments_by_range(string_to_date(start_date), string_to_date(end_date))
        return Participant.objects.filter(player = F('tournament__champion'),tournament__in = tournaments
        ).values('deck__archetype').annotate(count = Count('deck__archetype')).order_by('-count')
        
    def place_with_more_champions(start_date, end_date):
        tournaments = TournamentQueries.tournaments_by_range(string_to_date(start_date), string_to_date(end_date))
        queryset1 = tournaments.values('champion__municipe').annotate(
            amount=Count('champion__municipe')).order_by('-amount').first()
        queryset = tournaments.values('champion__province').annotate(
            amount=Count('champion__province')).order_by('-amount').first()
        return {"municipe": queryset1['champion__municipe'], "province": queryset['champion__province']}
    
    def archetypes_used():
         return Deck.objects.filter(id__in = Participant.objects.all().values(
            'deck')).distinct().values('archetype').annotate(amount = Count('archetype')).order_by('-amount')
        
        
class RoundQueries(AbstractQueries):
    instance= Round
    
    def create(self, name, tournament):
        # tournament = TournamentQueries().get(1)
        return self.instance.objects.create(tournament=tournament, name=name) 
    
    def create_matchs(round, players):
            count=0
            print(players)
            
            for i in players:
                for j in players[1:]:
                    print("no entre",i,j)
                    match_date = DateQueries().get_or_create(2000+count,1,1)
                    count+=1
                    MatchQueries().create( i, j, round, match_date)
                    
    def end_round(tournament):
            return tournament.rounds.last().matchs.count() == 1
        
    def is_empty(tournament):
        print("cant rondas",  tournament.rounds.count())
        return tournament.rounds.count() == 0
    
    def most_represented_archetypes(round_id):
        round = RoundQueries().get(round_id)
        matchs= Match.objects.filter(round = round)
        decks =  (Deck.objects.filter(id__in = matchs.values('player1__deck'))|Deck.objects.filter(id__in = matchs.values('player2__deck'))).distinct()
        return decks.values('archetype').annotate(count=Count('archetype')).order_by('-count')



       
class DateQueries(AbstractQueries):
    instance = Date
    
    def get_or_create(self, year,month,day):
        date =datetime.date(year,month,day)
        result,created= self.instance.objects.get_or_create(date=date)
        return result
            
           
class ParticipantQueries(AbstractQueries):
    instance= Participant
    
    def create(self, tournament, player, deck, registration_date):
         self.instance.objects.create(tournament =tournament, player = player,
                                       deck = deck, registration_date = registration_date)    

    def get_by_player_and_tournament(self,tournament_id, player_id):
        try:
            print("----",self.instance)
            result= self.instance.objects.get(player_id=player_id, tournament_id=tournament_id )
        except ObjectDoesNotExist:
            print("Either the result doesn't exist.")  
            result = None   
        except OperationalError:
            print("no such table: data_playe.")
            result = None   
        return result

class MatchQueries(AbstractQueries):
    instance= Match
    
    def create(self, player1, player2, round, match_date):
        self.instance.objects.create(player1=player1, player2=player2,
                             round=round, date=match_date)
        
    def update(self, match_id, champion_id, result):
        champion = ParticipantQueries().get(champion_id)
        print(champion.id)
        match = self.get(match_id)
        print(match)
        match.winner =champion
        match.result =result
        match.save()
