from django.urls import path
from . import views

urlpatterns = [
    path('', views.GalleryView.as_view(), name='gallery'),
    path('<int:pk>', views.GalleryDetailView.as_view(), name='gallery_detail'),
    path('', views.VideoView.as_view(), name='video'),
]