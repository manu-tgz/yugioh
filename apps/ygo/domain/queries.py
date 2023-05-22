from ..data.models import Deck, DeckCards, Card, Archetype
from apps.users.domain.queries import PlayerQueries 
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from django.db import OperationalError
import operator
from apps.abstract.domain.queries import AbstractQueries


class DeckQueries():
    def gb_player(value_list, count_var ):
        queryset=Deck.objects.all().values(value_list).annotate(amount=Count(count_var)).order_by('-amount')
        return queryset
    
    def create(self, name,player_id, cards):
        archetype_name = self.find_archetype(cards)
        player = PlayerQueries().get(player_id)
        archetype = ArchetypeQueries.get_archetype(archetype_name)
        deck, created = Deck.objects.get_or_create(name=name, player= player, archetype= archetype, main_deck=1
                                                   ,extra_deck=1, side_deck=1)
        if created is False:
           deck.main_deck, deck.extra_deck,deck.side_deck = DeckCardsQueries().create(deck,cards)
           deck.save()
    
    def get_deck(id):
        return Deck.objects.get(id=id)
    
    def find_archetype(self, card_list):
        archetype = {}
        for card in card_list:
            b =  CardQueries().get(card["card_id"]).archetype
            if archetype.get(b,None) is None:
                archetype[b]=1
            else: 
                archetype[b]+=1
        max_key = max(archetype.items(), key=operator.itemgetter(1))[0] 
        return max_key  
        
    
class ArchetypeQueries():
    def most_popular():
        queryset = Deck.objects.all().values('archetype').annotate(amount=Count('id')).order_by('-amount')
        return queryset
    
    # TODO: Use dynamic filters not to repeat method for province and municipality
    def most_popular_in_province(province):        
        queryset = Deck.objects.all().values('archetype').annotate(
            amount=Count('id')).filter(player__province= province).order_by('-amount')
        return queryset
    
    def most_popular_in_municipe(municipe):        
        queryset = Deck.objects.all().values('archetype').annotate(
            amount=Count('id')).filter(player__municipe= municipe).order_by('-amount')
        return queryset

    def get_archetype(archetype_name):
        try:
            archetype =Archetype.objects.get(name=archetype_name)
        except ObjectDoesNotExist:
            print("Either the archetype doesn't exist.")  
            archetype = None   
        except OperationalError:
            print("no such table: data_playe.")
            archetype = None   
        return archetype     
    
    def municipe_popular(archetype_id):
        queryset1 = Deck.objects.all().values('player__municipe').annotate(
            amount=Count('archetype')).filter(archetype_id= archetype_id).order_by('-amount').first()
        
        queryset = Deck.objects.all().values('player__province').annotate(
            amount=Count('archetype')).filter(archetype_id= archetype_id).order_by('-amount').first()
        return {"municipe": queryset1['player__municipe'], "province": queryset['player__province']}

class CardQueries(AbstractQueries):
    instance = Card
    def create(self, name, class_type, archetype):
        self.instance.objects.create(name=name, class_type=class_type, archetype=archetype)
        
class DeckCardsQueries(AbstractQueries):
    instance = DeckCards
    def create(self,deck, card_list):
        MD_count,SD_count,ED_count=0,0,0
        
        for card in card_list:
            c = CardQueries().get(card["card_id"])
            MD, ED, SD = False,False,False
            site = card["site"]
            if site =="MD":
                MD = True
                MD_count+=1
            elif site =="ED":
                ED = True
                ED_count+=1
            elif site=="SD":
                SD= True
                SD_count+=1
            self.instance.objects.create(deck=deck, card= c,
                                         MD=MD, ED=ED, SD=SD)
        
        return MD_count,ED_count,SD_count

# a = [{"card_id":3, "site":"MD"},{"card_id":4, "site":"MD"},{"card_id":3, "site":"ED"},{"card_id":2, "site":"SD"}]

# DeckQueries().create("Nw1tR",2,a)
# # c= ArchetypeQueries