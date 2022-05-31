# Render allows you to pass back a template that turns into an HttpResponce
from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.


def home(request):
    return render(request, 'generator/home.html')
    # I can reference any of the items in this dictionary in my home.html


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))  # 12 is the default now

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    # Request - test
    return render(request, 'generator/about.html')
