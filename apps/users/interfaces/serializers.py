from rest_framework import serializers 
from ..data.models import Player

class PlayerSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Player 
        fields = ('user_id','name')
