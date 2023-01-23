from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='main'),
    path('about', views.about, name='about'),
    path('staff', views.staff, name='staff'),
]