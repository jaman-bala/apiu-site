from django.urls import path
from . import views

urlpatterns = [
    path('', views.online, name='online'),
]