from django.contrib import admin
from .models import User
from myapi.models import Input

admin.site.register(User)
admin.site.register(Input)
# Register your models here.
