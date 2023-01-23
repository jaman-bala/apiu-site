from django.shortcuts import render
from .models import Photo
from .staff import Staff
from .additional import Video
from ..news.models import Articles
from backend.apps.news.models import Articles
    

def index(request):
    video = Video.objects.all()
    photos = Photo.objects.all()
    news = Articles.objects.all()
    context = {
        "photos":photos,
        "video":video,
        "news": news,
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')   


def staff(request):
    staff = Staff.objects.all()
    context = {
        "staff": staff,
    }
    return render(request, 'main/staff.html', context) 