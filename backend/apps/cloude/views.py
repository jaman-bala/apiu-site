from django.shortcuts import render
from .models import Photo


def index(request):
    photo = Photo.objects.all()
    return render(request, 'main/index.html', {'photo': photo} )

def about(request):
    return render(request, 'main/about.html')    