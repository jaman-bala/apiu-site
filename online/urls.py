from django.urls import path
from . import views

urlpatterns = [
    path('online', views.online, name='online'),
    path('', views.create, name='create'),
]