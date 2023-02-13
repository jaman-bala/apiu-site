from django.urls import path
from . import views

urlpatterns = [
    path('', views.TenderView.as_view(), name='tender'),
    path('<int:pk>', views.TenderDetailView.as_view(), name='tender_detail'),
    path('vacancy/', views.VacancyView.as_view(), name='vacancy'),
    path('vacancy/<int:pk>', views.VacancyDetailView.as_view(), name='vacancy_detail'),
    path('other/', views.OtherView.as_view(), name='other'),
    path('<int:pk>', views.OtherDetailView.as_view(), name='other_detail'),

]