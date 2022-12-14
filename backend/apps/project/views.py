from django.shortcuts import render
from .models import File


def project(request):
    project = File.objects.all()
    return render(request, 'project/project.html', {'project': project} )



