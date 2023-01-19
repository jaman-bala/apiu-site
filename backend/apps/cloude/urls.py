from django.urls import path
from .views import create_folder, upload_file, folder_list, folder_detail

urlpatterns = [
    path('create/', create_folder, name='create_folder'),
    path('upload/', upload_file, name='upload_file'),
    path('', folder_list, name='folder_list'),
    path('<int:folder_id>/', folder_detail, name='folder_detail'),
]
