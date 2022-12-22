from django.shortcuts import render
from .models import Photo
from .additional import Info
from django.views.generic import ListView
    

def index(request):
    informations=Info.objects.all()
    photo = Photo.objects.all()
    context = {
        "photo":photo,
        "informations":informations
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')    