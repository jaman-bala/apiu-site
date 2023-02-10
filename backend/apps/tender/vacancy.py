from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Vacancy(models.Model):
    country = models.CharField("Страна",  max_length=250)
    title = models.CharField("Название проекта", max_length=250)
    text = RichTextUploadingField("Текст")
    file = models.FileField(upload_to='files', blank=True, verbose_name="Добавить файл")
    is_active = models.BooleanField("Активный", default = True)
    date = models.DateTimeField('Срок подачи заявок')
    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)



    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Ваканция'
        verbose_name_plural = 'Ваканции'