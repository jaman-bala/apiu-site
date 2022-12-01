from django.shortcuts import render, redirect
from .models import Create
from .forms import CreateForm
from django.views.generic import DetailView


def create(request):
    error = ''
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('online')
        else:
            error = 'Формат был неверной'

    form = CreateForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'online/create.html', data )


def online(request):
    task = Create.objects.order_by('-id')
    return render(request, 'online/online.html', {'task': task})


