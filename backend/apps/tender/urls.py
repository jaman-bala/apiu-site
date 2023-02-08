from django.urls import path
from . import views

urlpatterns = [
    path('', views.tender, name='tender'),
    path('vacancy/', views.vacancy, name='vacancy'),
    path('other/', views.other, name='other'),

]