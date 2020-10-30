from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')


def menu(request):
    return render(request, 'menu.html')


def about(request):
    return render(request, 'about.html')


def grocessory(request):
    return render(request, 'grocess.html')


def fruit(request):
    return render(request, 'fruit.html')


def giraj(request):
    return render(request, 'giraj_pd.html')