from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Folder(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Папка'
        verbose_name_plural = 'Добавить папку'

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=now)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Добавить файд'


