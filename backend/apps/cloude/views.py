from django.shortcuts import render
from .models import Photo
from .additional import Info
from django.views.generic import ListView


class InfoView(ListView):
        model = Info.objects.all()
        template_name = 'main/index.html'
        context_object_name = 'informations'
        

def index(request):
    photo = Photo.objects.all()
    return render(request, 'main/index.html', {'photo': photo})

def about(request):
    return render(request, 'main/about.html')    