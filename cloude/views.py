from django.shortcuts import render
from .models import Photo

# Create your views here.
def index(request):
    photo = Photo.objects.all()
    return render(request, 'main/index.html', {'photo': photo} )

def about(request):
    return render(request, 'main/about.html')    