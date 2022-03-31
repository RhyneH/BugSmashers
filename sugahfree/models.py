from os import access
from django.db import models
from django.contrib.auth.models import AbstractUser

# class Item(models.Model):
#     access_token = models.CharField(max_length=100)


class User(AbstractUser):
    pass

class Input(models.Model):
    insulin = models.CharField(max_length=50)
    carbs = models.CharField(max_length=50)
    food_intake = models.TextField(blank=False)

def __str__(self):
    return self.input    
# Create your models here.
