from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView, ListView


class NewshomeView(ListView):
        model = Articles
        template_name = 'news/news_home.html'
        context_object_name = 'news'
        paginate_by = 5
        queryset = Articles.objects.all()

# def news_home(request):
#     news = Articles.objects.order_by('-date')
#     return render(request, 'news/news_home.html', {'news': news} )


class NewsDetailView(DetailView):
        model = Articles
        template_name = 'news/details_view.html'
        context_object_name = 'article'