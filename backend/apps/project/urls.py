from django.urls import path
from . import views

urlpatterns = [
    path('', views.project, name='project'),
    path('disain/', views.disain, name='disain'),
    path('report/', views.report, name='report'),
    path('study/', views.study, name='study'),
]