from os import access
from django.db import models
from sugahfree.models import User

class Input(models.Model):
    insulin_in_units = models.CharField(max_length=50)
    carbs_in_grams = models.CharField(max_length=50)
    food_intake = models.TextField(blank=False)
    user = models.ForeignKey(User, related_name= 'inputs', on_delete= models.CASCADE)
    created = models.DateTimeField(auto_now_add= True)

def __str__(self):
    return self.insulin    


