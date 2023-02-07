from .models import Articles
from django.views.generic import DetailView, ListView


class NewshomeView(ListView):
        model = Articles
        template_name = 'news/news_home.html'
        context_object_name = 'news'
        paginate_by = 15
        queryset = Articles.objects.all()


class NewsDetailView(DetailView):
        model = Articles.objects.all()
        template_name = 'news/details_view.html'
        context_object_name = 'article'
        queryset = Articles.objects.all()