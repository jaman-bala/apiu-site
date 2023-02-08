from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.apps.main.urls')),
    path('news/', include('backend.apps.news.urls')),
    path('online/', include('backend.apps.online.urls')),
    path('account/', include('backend.apps.account.urls')),
    path('books/', include('backend.apps.library.urls')),
    path('project/', include('backend.apps.project.urls')),
    path('cloude/', include('backend.apps.cloude.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('gallery/', include('backend.apps.gallery.urls')),
    path('gallery/', include('backend.apps.tender.urls')),
    
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
