from os import access
from django.db import models
from sugahfree.models import User

class Input(models.Model):
    blood_sugar = models.IntegerField()
    carbs_in_grams = models.IntegerField()
    food_intake = models.TextField(blank=False)
    user = models.ForeignKey(User, related_name= 'inputs', on_delete= models.CASCADE)
    created = models.DateTimeField(auto_now_add= True)

    @property
    def calculate_insulin_units(self):
        units_of_insulin = self.carbs_in_grams//20
        if self.blood_sugar > 200: 
            units_of_insulin += 1
        return units_of_insulin
           


    def __str__(self):
        return self.insulin_in_units  


