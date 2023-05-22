from rest_framework import serializers 

class DeckSerializer(serializers.Serializer):
    """Serializer definition for Deck."""
    name = serializers.CharField()
    player_id = serializers.IntegerField()
    cards = serializers.ListField() 

class CardSerializer(serializers.Serializer):
    """Serializer definition for Card."""
    name = serializers.CharField()
    class_type = serializers.CharField()
    archetype = serializers.CharField()
    
class DeckCardsSerializer(serializers.Serializer):
    """Serializer definition for Card."""
    card_id = serializers.IntegerField()
    site = serializers.CharField()
    
class GBPlayerSerializer(serializers.Serializer):
    player = serializers.IntegerField()
    amount = serializers.IntegerField()
 
class ArchetypeSerializer(serializers.Serializer):
    archetype = serializers.CharField()
    
class GBArchetypeSerializer(serializers.Serializer):
    archetype = serializers.CharField()
    amount = serializers.IntegerField()
    
class PlaceSerializer(serializers.Serializer):
    municipe = serializers.CharField()
    province = serializers.CharField()
    
    


