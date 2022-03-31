from django.shortcuts import render
from django.http import JsonResponse 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Input 

def index(request):
    input = Input.objects.all()
    return render(request, 'sugahfree/home.html')

# Create your views here.
