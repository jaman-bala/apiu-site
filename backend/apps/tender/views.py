from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Tender
from .vacancy import Vacancy
from .other import Other
# Create your views here.


#Tender
class TenderView(ListView):
    model = Tender
    template_name = 'tender/tender.html'
    context_object_name = 'tender'
    paginate_by = 40
    queryset = Tender.objects.all()

class TenderDetailView(DetailView):
    model = Tender.objects.all()
    template_name = 'tender/tender_detail.html'
    context_object_name = 'tender_detail'
    queryset = Tender.objects.all()


#Vacancy
class VacancyView(ListView):
    model = Vacancy
    template_name = 'tender/vacancy.html'
    context_object_name = 'vacancy'
    paginate_by = 40
    queryset = Vacancy.objects.all()

class VacancyDetailView(DetailView):
    model = Vacancy.objects.all()
    template_name = 'tender/vacancy_detail.html'
    context_object_name = 'vacancy_detail'
    queryset = Vacancy.objects.all()


#Other
class OtherView(ListView):
    model = Other()
    template_name = 'tender/other.html'
    context_object_name = 'other'
    paginate_by = 40
    queryset = Other.objects.all()

class OtherDetailView(DetailView):
    model = Other.objects.all()
    template_name = 'tender/other_detail.html'
    context_object_name = 'other_detail'
    queryset = Other.objects.all()



