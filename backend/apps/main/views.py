from django.shortcuts import render
from .models import Photo
from .staff import Staff
from .additional import Video
from ..news.models import Articles
from ..gallery.models import Gallery
from backend.apps.news.models import Articles
    

def index(request):
    video = Video.objects.all()[:2]
    gallery = Gallery.objects.all()[:2]
    photos = Photo.objects.all()[:1]
    news = Articles.objects.all()[:4]        # если добавить то только выйдет 6 информации[:6]
    context = {
        "photos":photos,
        "video":video,
        "news": news,
        "gallery": gallery,
    }
    return render(request, 'main/index.html', context)

    


def about(request):
    return render(request, 'main/about.html')   

def search(request):
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        if query:
            object_list = Library.objects.filter(
                Q(author__icontains=query) | Q(title__icontains=query)
            )
            return render(request, 'books/books.html')
            object_list1 = Articles.objects.filter(
                Q(author__icontains=query) | Q(title__icontains=query)
            )
            return render(request, 'news/news_home.html')
            object_list2 = Gallery.objects.filter(
                Q(author__icontains=query) | Q(title__icontains=query)
            )
            return render(request, 'gallery/gallery.html')

        else:
            object_list = Library.objects.all()
            object_list1 = Articles.objects.all()
            object_list2 = Gallery.objects.all()
        return object_list
    return render(request, 'main/search.html')  


def staff(request):
    staff = Staff.objects.all()
    context = {
        "staff": staff,
    }
    return render(request, 'main/staff.html', context) 