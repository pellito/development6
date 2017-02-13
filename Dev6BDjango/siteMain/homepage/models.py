from django.db import models
from django.shortcuts import render


def index(request):
    return render(request, 'loggedin/home.html')

# Create your models here.
