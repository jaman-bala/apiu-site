from django.urls import path
from .views import create_folder, upload_file, folder_list, folder_detail, download_file, delete_file

urlpatterns = [
    path('create/', create_folder, name='create_folder'), # Создание папки
    path('upload/', upload_file, name='upload_file'), # Добавление файла в папку
    path('', folder_list, name='folder_list'), # Список папок
    path('<int:folder_id>/', folder_detail, name='folder_detail'), # Деталии
    path('download_file/<int:file_id>/', download_file, name='download_file'),
    path('delete_file/<int:file_id>/', delete_file, name='delete_file'),
]
