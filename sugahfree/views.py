import json
from django.forms import forms
from django.shortcuts import render
from django.http import JsonResponse 
from django.shortcuts import render, redirect, get_object_or_404
from myapi.models import Input
from .forms import InputForm

def index(request):
    input = Input.objects.all()
    form = InputForm()
    return render(request, 'sugahfree/home.html')

def add_input(request):
    if request.method == "POST":
        print(request.POST)
        form = InputForm(request.POST)
        if form.is_vaild():
            new_input = form.save()
            return redirect("home")
    else:
        form = InputForm()
    return render(request, 'sugahfree/add_input.html', {'form': form})



