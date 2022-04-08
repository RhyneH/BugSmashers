from django.forms import ModelForm
from myapi.models import Input

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['insulin_in_units', 'carbs_in_grams', 'food_intake']
        