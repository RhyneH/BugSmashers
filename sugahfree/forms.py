from django.forms import ModelForm
from myapi.models import Input

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['blood_sugar', 'carbs_in_grams', 'food_intake']
        