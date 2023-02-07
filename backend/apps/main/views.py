from django.shortcuts import render
from .models import Photo
from .staff import Staff
from .additional import Video
from ..news.models import Articles
from ..gallery.models import Gallery
from backend.apps.news.models import Articles
    

def index(request):
    video = Video.objects.all()[:3]
    gallery = Gallery.objects.all()[:5]
    photos = Photo.objects.all()
    news = Articles.objects.all()        # если добавить то только выйдет 3 информации[:3]
    context = {
        "photos":photos,
        "video":video,
        "news": news,
        "gallery": gallery,
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