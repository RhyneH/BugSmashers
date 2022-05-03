from typing import ContextManager
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import InputSerializer 
from .models import Input 
import math

class InputViewSet(viewsets.ModelViewSet):
    serializer_class = InputSerializer


    def get_queryset(self):
        return self.request.user.inputs.all().order_by('-created')

