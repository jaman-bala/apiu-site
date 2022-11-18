from django.shortcuts import render
from .models import Online
# Create your views here.


def online(request):
    online = Online.objects.all()
    return render(request, 'online/online.html', {'online': online} )