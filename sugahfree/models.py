# from os import access
# from django.db import models
from django.contrib.auth.models import AbstractUser
# # from django.contrib.auth.models import User



class User(AbstractUser):
    pass

# class Input(models.Model):
#     insulin = models.CharField(max_length=50)
#     carbs = models.CharField(max_length=50)
#     food_intake = models.TextField(blank=False)
#     user = models.ForeignKey(User, related_name= 'inputs', on_delete= models.CASCADE)
#     created = models.DateTimeField(auto_now_add= True)

# def __str__(self):
#     return self.input    
# # Create your models here.
