from django.shortcuts import render
from .models import Library
from django.views.generic import TemplateView, ListView, DetailView



class LibraryView(ListView):
    model = Library
    template_name = "library/library.html"
    context_object_name = "books"

    

