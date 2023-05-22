from rest_framework import serializers 

class TournamentSerializer(serializers.Serializer):
    name = serializers.CharField()
    manager = serializers.IntegerField()
    address = serializers.CharField()
    start_date = serializers.CharField()
    
    
    # start_date = serializers.DateField(allow_null= True,  format="%Y-%m-%d",
    #                                     input_formats=["%Y-%m-%d"])
    # finish_date = serializers.DateField(allow_null= True,  format="%Y-%m-%d",
    #                                     input_formats=["%Y-%m-%d"]) 
    
    # def validate(self, value):
    #     return value.strftime('%Y-%m-%d') if value else value

class ParticipantSerializer(serializers.Serializer):
    player_id = serializers.CharField()
    deck_id = serializers.CharField()
    date= serializers.DateField()

class RegistertSerializer(serializers.Serializer):
    tournament_id = serializers.IntegerField()
    players = serializers.ListField(child=serializers.DictField(),  min_length=1,
                                    max_length=None)
    

class RoundSerializer(serializers.Serializer):
    name = serializers.CharField()
    tournament_id = serializers.IntegerField()
    
    
class MatchSerializer(serializers.Serializer):
    champion_id = serializers.IntegerField()
    match_id = serializers.IntegerField()
    result = serializers.CharField()
    
    
    

# b = a.data