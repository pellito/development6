from django.shortcuts import render
import multiprocessing
from cooldown import cooldown


def index(request):
    return render(request, 'homepage/header.html')


