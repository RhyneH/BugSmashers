from django.forms import ModelForm
from myapi.models import Input

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['insulin', 'carbs', 'food_intake']