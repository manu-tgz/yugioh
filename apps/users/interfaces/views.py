# from rest_framework import generics, permissions  
# from .models import Player, User 
# # from .permissions import IsPlayerOrReadOnly
# from .serializers import PlayerSerializer, UserSerializer  
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import viewsets


# class CreateUser(APIView):
#     """
#     Create users.
#     """
#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides `list` and `retrieve` actions.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides `list` and `retrieve` actions.
#     """
#     queryset = Player.objects.all()
#     serializer_class = PlayerSerializer   
    
    
    
# # class PlayerList(generics.ListCreateAPIView):
# #     """_summary_
# #     to provide the .list() and .create() actions.
# #     get: list, post: create
    
# #     Args:
# #         pk: for get - List
# #         player: for post - Create
# #     """
# #     queryset = Player.objects.all() 
# #     serializer_class = PlayerSerializer
    
# # class DetailPlayer(generics.RetrieveUpdateDestroyAPIView): 
# #     """_summary_
# #     to provide the .retrieve(), .update() and .destroy() actions.
# #     get: retrieve, put: update, delete: destroy
    
# #     Args:
# #         pk: for get - Retrieve and for destroy - Delete
# #         player: for post - Update
# #     """
# #     # permission_classes =(IsPlayerOrReadOnly,)
# #     queryset = Player.objects.all() 
# #     serializer_class = PlayerSerializer


