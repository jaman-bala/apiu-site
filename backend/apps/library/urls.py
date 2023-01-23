
from django.urls import path
from . import views

urlpatterns = [
    path("", views.LibraryView.as_view(), name='books'),
    

]