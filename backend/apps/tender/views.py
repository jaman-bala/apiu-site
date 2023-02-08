from django.shortcuts import render
from .models import Tender
from .vacancy import Vacancy
from .other import Other
# Create your views here.




def tender(request):
    tender = Tender.objects.all()
    context = {
        "tender": tender
    }
    return render(request, 'tender/tender.html', context )


def vacancy(request):
    vacancy = Vacancy.objects.all()
    context = {
        "vacancy": vacancy
    }
    return render(request, 'tender/vacancy.html', context)


def other(request):
    other = Other.objects.all()
    context = {
        "other": other
    }
    return render(request, 'tender/other.html', context)