from django.shortcuts import render
from .models import Library
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin



class LibraryView(LoginRequiredMixin, ListView):
    model = Library
    template_name = "books/books.html"
    context_object_name = "books"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        if query:
            object_list = Library.objects.filter(
                Q(author__icontains=query) | Q(title__icontains=query)
            )
        else:
            object_list = Library.objects.all()
        return object_list

    

