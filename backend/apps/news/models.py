from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Articles(models.Model):
    title = models.CharField('Название', max_length=200)
    full_text = RichTextUploadingField('Статья')
    img = models.ImageField('Добавить фото', upload_to='img', blank=True)
    date = models.DateTimeField('Дата публикации')
    is_active = models.BooleanField("Активный", default=True)
    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)


    def __str__(self):
        return self.title


    class Meta:
        ordering = ["-created"]
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'