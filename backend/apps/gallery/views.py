from .models import Gallery
from django.db.models import Q
from django.views.generic import DetailView, ListView
from .models import Video


class GalleryView(ListView):
    model = Gallery
    template_name = 'gallery/gallery.html'
    context_object_name = 'gallery'
    paginate_by = 100
    queryset = Gallery.objects.all()

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        if query:
            object_list = Gallery.objects.filter(
                Q(country__icontains=query) | Q(title__icontains=query) | Q(date__icontains=query)
            )
        else:
            object_list = Gallery.objects.all()
        return object_list


class GalleryDetailView(DetailView):
    model = Gallery.objects.all()
    template_name = 'gallery/gallery_detail.html'
    context_object_name = 'gallery_detail'
    queryset = Gallery.objects.all()


class VideoView(ListView):
    model = Video.objects.all()
    template_name = "gallery/video.html"
    context_object_name = 'videos_gallery'
    paginate_by = 100
    queryset = Video.objects.all()

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        if query:
            object_list = Video.objects.filter(
                Q(country__icontains=query) | Q(title__icontains=query) | Q(date__icontains=query)
            )
        else:
            object_list = Video.objects.all()
        return object_list
