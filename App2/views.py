from django.shortcuts import render
from .models import *

# Create your views here.
def  homePage(request):
    planets = Planet.objects.all()
    context = {"planetInfo": planets}
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")


def homePage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')