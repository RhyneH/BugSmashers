from django.forms import ModelForm
from .models import Input

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['insulin', 'carbs', 'food_intake']