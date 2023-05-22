from django.core.exceptions import ObjectDoesNotExist
from django.db import OperationalError

class AbstractQueries:
    instance= None
    primary_key=None
    def get(self, id):
        try:
            result= self.instance.objects.get(id=id)
        except ObjectDoesNotExist:
            print("Either the result doesn't exist.")  
            result = None   
        except OperationalError:
            print("no such table: data_playe.")
            result = None   
        return result
    