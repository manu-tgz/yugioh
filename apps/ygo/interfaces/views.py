from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .serializers import *
from rest_framework.response import Response
from ..usecases.deck import DeckUseCases
from ..usecases.archetype import ArchetypeUseCases
from ..domain.queries import DeckQueries, ArchetypeQueries
# from django.http import JsonResponse

  
class ArchetypeGBPlace( ListAPIView):
    serializer_class = GBArchetypeSerializer
    
    def get(self, request, *args, **kwargs):
        province = request.query_params.get('province',0)
        municipe = request.query_params.get('municipe',0)
        print("municipe:", municipe, "province:", province)
        if province != 0:        
            self.queryset = ArchetypeUseCases.most_popular_in_province(province) 
        elif municipe !=0:        
            self.queryset = ArchetypeUseCases.most_popular_in_municipe(municipe) 
     
        return super().get(request, *args, **kwargs)
    
        
class DeckCreateView(CreateAPIView):
    serializer_class  = DeckSerializer
    
    def perform_create(self, serializer):
        data = serializer.data
        DeckQueries().create(name=data['name'], player_id= data['player_id'],
                           cards= data['cards'] )
        
        
class DeckGBPlayer(ListAPIView):
    serializer_class = GBPlayerSerializer
    queryset = DeckUseCases.player_amount()
    
    
class PlacePopulateArchetype(RetrieveAPIView): 
    serializer_class = PlaceSerializer
    
    def retrieve(self, request, *args, **kwargs):
        archetype = request.query_params.get('archetype',0)
        self.queryset = ArchetypeQueries.municipe_popular(archetype)        
        serializer = self.get_serializer(self.queryset)
        return Response(serializer.data)

# def PlacePopulateArchetype(request):
#     print(request)
#     archetype = request.query_params.get('archetype',0)
#     queryset  = ArchetypeQueries.municipe_popular(archetype)
#     return JsonResponse(queryset,safe = False)
   
class ArchetypeGBPlayer(ListAPIView):
    serializer_class = GBArchetypeSerializer
    queryset = ArchetypeQueries.most_popular()
    
class CardCreateView(CreateAPIView):
    serializer_class  = CardSerializer
    
    def perform_create(self, serializer):
        data = serializer.data
        DeckQueries().create(name=data['name'], player_id= data['player_id'], main_deck=data['main_deck'],
                           extra_deck= data['extra_deck'], side_deck= data['side_deck'],
                           cards= data['cards'] )    
    
# queryset = Deck.objects.all().values('archetype', 'archetype_id').annotate(
#              amount=Count('id')).filter(player__province= 'SS').order_by('-amount')        
       

