import datetime
from filecmp import clear_cache
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.development')

import django
django.setup()

from apps.ygo.data.models import Deck,Archetype, Card
from apps.users.data.models import Player, User, Manager
from apps.tournament.data.models import Date, Participant, Tournament, Round, Match
import random
       
def create_deck(name, player, main_deck, side_deck, extra_deck, archetype):
        deck, created = Deck.objects.get_or_create(name=name, player= player, main_deck=main_deck, extra_deck=extra_deck, 
                        side_deck=side_deck, archetype= archetype)
        return deck

def create_player(name,user,province,municipe,  country, address, phone_number=12 ):
    player, created=  Player.objects.get_or_create( name=name, user=user,  phone_number=phone_number,
                          province=province,country= country,municipe=municipe, address = address)
    return player

def create_card(name,class_type,archetype):
    card = Card.objects.create(name=name, class_type=class_type,archetype = archetype )
    return card
   
def create_user(email,first_name,last_name,username):
    ua, created= User.objects.get_or_create(email=email, first_name=first_name,
                                            last_name=last_name, username=username)
    return ua

def create_archetype(name):
    archetype, created =  Archetype.objects.get_or_create( name=name)
    return archetype  

def create_tournament(name,start_date,finish_date,address,champion=None):
    t1, created= Tournament.objects.get_or_create(name=name,start_date=start_date,
                                                  finish_date=finish_date,address = address, champion = champion) 
    return t1

def run():
    
    for num in range(5):
        ua, created= User.objects.get_or_create(email="email{}".format(num), first_name="name{}".format(num),
                                            last_name="lt{}".format(num), username="{}".format(num))
        ub, created= User.objects.get_or_create(email="email{}_{}".format(num,num), first_name="name{}_{}".format(num,num),
                                            last_name="lt{}_{}".format(num,num), username="{}_{}".format(num,num))
        uc = create_user("email{}_{}_{}".format(num,num,num),"name{}_{}_{}".format(num,num,num),"lt{}_{}".format(num,num), 
                         "{}_{}_{}".format(num,num,num))     
        pl1, created=  Player.objects.get_or_create( name="player{}_{}".format(num,num), user=ub,  phone_number=num*1000,
                          province= "P{}_{}".format(num,num),country= "C{}_{}".format(num,num), municipe= "M{}_{}".format(num,num),
                           address = "Brasil")
        
        pl = create_player("player{}".format(num),ua, "P{}".format(num), "M{}".format(num), "Cuba",num)
        pl2 = create_player("playerb{}".format(num),uc, "P{}".format(num), "M{}".format(num), "Cuba",num)
        
        
        aaa, created =  Archetype.objects.get_or_create( name="a{}".format(num))
        bbb = create_archetype("b{}".format(num))
        ccc = create_archetype("c{}".format(num))
        
        card = create_card("card{}".format(num), "Monster",aaa)

        dka = create_deck("Magos{}".format(num), pl, 3,2,1, aaa )
        dkd = create_deck("Bestia{}".format(num), pl, 3,2,1, aaa )
        dke = create_deck("Dragon{}".format(num), pl, 3,2,1, bbb )
        dkc = create_deck("Maquina{}".format(num), pl, 3,2,1, ccc )
        
        dkb= create_deck("Hechizo{}".format(num), pl1, 3,2,1, aaa )
        dkc1= create_deck("Mortal{}".format(num), pl1, 3,2,1, bbb )
        dkf = create_deck("Bestia{}".format(num), pl1, 3,2,1, aaa )
        
        dka2= create_deck("Fuego{}".format(num), pl2, 3,2,1, ccc )
        dkb2= create_deck("Aire{}".format(num), pl2, 3,2,1, bbb )
        
        ma, created = Manager.objects.get_or_create(name="manager{}".format(num), user=ua)
        
        da, created= Date.objects.get_or_create(date=datetime.date(2000+num, 1, 1))
        db, created= Date.objects.get_or_create(date=datetime.date(1900+num, 1, 1)) 
        ta, created= Tournament.objects.get_or_create(name="tournament{}".format(num),
                                                      start_date= datetime.date(2000+num, 1, 1),
                                                      finish_date=datetime.date(2000+num, 1, 1),
                                                      address = "D{}".format(num), champion=pl)
        t1, created= Tournament.objects.get_or_create(name="tournament{}_{}".format(num,num),
                                                      start_date= datetime.date(2000+num, 1, 1),
                                                      finish_date=datetime.date(2000+num, 1, 1),
                                                      address = "D{}".format(num), champion = pl1)
        ta.save()
        ta.managers.add(ma)
        ta.save()
        
        ra, created= Round.objects.get_or_create(name="Ronda{}".format(num), tournament=ta)
        
        pa, created= Participant.objects.get_or_create( tournament=ta,
                    registration_date=da, deck= dka, player= pl )
        pb, created= Participant.objects.get_or_create(tournament=ta,
                    registration_date=db, deck= dkb, player= pl1 )  
        
        pa1, created= Participant.objects.get_or_create( tournament=t1,
                    registration_date=da, deck= dka, player= pl )
        pb1, created= Participant.objects.get_or_create(tournament=t1,
                    registration_date=db, deck= dkb, player= pl1 )  

        mt, created= Match.objects.get_or_create( round=ra,  date=da,
                                player1=pa, player2=pb, winner=pb)
        
        if num == 4:
            t1, created= Tournament.objects.get_or_create(name="tournament{}_{}_{}".format(num,num,num),
                                                      start_date= datetime.date(2000+num, 1, 1),
                                                      finish_date=datetime.date(2000+num, 1, 1),
                                                      address = "D{}".format(num), champion = pl2)
            pa, created= Participant.objects.get_or_create( tournament=t1,
                    registration_date=da, deck= dka2, player= pl2 )
