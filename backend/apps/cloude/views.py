from django.shortcuts import render
from .models import Photo
from .additional import Info
from ..news.models import Articles
    

def index(request):
    informations = Info.objects.all()
    photo = Photo.objects.all()
    news = Articles.objects.all()
    context = {
        "photo":photo,
        "informations":informations,
        "news": news,
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')    