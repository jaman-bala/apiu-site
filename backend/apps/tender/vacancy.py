from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Vacancy(models.Model):
    country = models.CharField("Страна",  max_length=250)
    title = models.CharField("Название проекта", max_length=250)
    text = RichTextUploadingField("Текст")


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Ваканция'
        verbose_name_plural = 'Ваканции'