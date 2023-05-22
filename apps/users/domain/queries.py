from ..data.models import Player, Manager
from apps.abstract.domain.queries import AbstractQueries
from django.core.exceptions import ObjectDoesNotExist
from django.db import OperationalError

class UserQueries(AbstractQueries):
    # TODO: agregar la variable primary_key a AbstractQueries y que se pueda usar
    # user_id para asi no necesitar esta clase
    
    def get(self, id):
        try:
            result= self.instance.objects.get(user_id=id)
        except ObjectDoesNotExist:
            print("Either the result doesn't exist.")  
            result = None   
        except OperationalError:
            print("no such table: data_playe.")
            result = None   
        return result

class PlayerQueries(UserQueries):
    instance = Player
    
class ManagerQueries(UserQueries):
    instance = Manager    

