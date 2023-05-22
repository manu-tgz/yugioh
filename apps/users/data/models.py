from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # TODO: El email debe ser unico
    REQUIRED_FIELDS = ['first_name', 'last_name','password']

    def say_hello(self):
        return "Hello, my name is {}".format(self.first_name)

class Player(models.Model):
    # TODO: Hacer que el user sea su primary key
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User,primary_key=True, verbose_name="user", on_delete=models.CASCADE)
    phone_number = models.PositiveIntegerField()
    country = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    municipe = models.CharField(max_length=30)
    address = models.CharField(max_length=80)   
    
    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Player_detail", kwargs={"pk": self.pk})


class Manager(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User,primary_key=True, verbose_name="user", on_delete=models.CASCADE)   

    # TODO: agregar grupo del manager con sus respectivas funciones
    
    class Meta:
        verbose_name = "Manager"
        verbose_name_plural = "Managers"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Manager_detail", kwargs={"pk": self.pk})




