from django.shortcuts import render
from .models import Create
from .forms import CreateForm



def create(request):
    error = ''
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Формат был неверной'

    form = CreateForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'online/create.html', data )


def online(request):
    return render(request, 'online/online.html')