from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import InputSerializer 
from .models import Input 


class InputViewSet(viewsets.ModelViewSet):
    queryset = Input.objects.all().order_by('-created')
    serializer_class = InputSerializer


# Create your views here.

