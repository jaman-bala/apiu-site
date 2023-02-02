from django.shortcuts import render
from .models import Gallery
from django.views.generic import DetailView, ListView


class GalleryView(ListView):
        model = Gallery
        template_name = 'gallery/gallery.html'
        context_object_name = 'gallery'
        paginate_by = 100
        queryset = Gallery.objects.all()


class GalleryDetailView(DetailView):
        model = Gallery.objects.all()
        template_name = 'gallery/gallery_detail.html'
        context_object_name = 'gallery_detail'
        queryset = Gallery.objects.all()
