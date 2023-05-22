from django.urls import path, include
# from .views import UserViewSet, PlayerViewSet
from rest_framework.routers import DefaultRouter


# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'players', PlayerViewSet,basename="player")
# router.register(r'', UserViewSet,basename="users")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # path('', include(router.urls)),
]


# # urlpatterns = [
# #    path("player/", PlayerListView.as_view(), name="home"),
# #    path('player/<int:pk>/', DetailPlayer.as_view(), name="player"), 
# # ]