from rest_framework import serializers 
from .models import Input

class InputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Input
        fields = ('insulin_in_units', 'carbs_in_grams', 'food_intake', 'user', 'created')