from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Other(models.Model):
    country = models.CharField("Страна",  max_length=250)
    title = models.CharField("Название проекта", max_length=250)
    text = RichTextUploadingField("Текст")
    is_active = models.BooleanField("Активный", default=True)
    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Другое'
        verbose_name_plural = 'Другие'