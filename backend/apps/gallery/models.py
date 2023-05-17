from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Gallery(models.Model):
    photo_add = models.ImageField('Фото', upload_to='img', blank=True,)
    title = models.CharField('Название', max_length=255, blank=True)
    country = models.CharField('Страна', max_length=255, blank=True)
    description = RichTextUploadingField('Статья')
    date = models.DateTimeField('Дата публикации')
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField("Активный", default=True)




    class Meta:
        ordering = ['-created']
        verbose_name = "Добавить"
        verbose_name_plural = "Добавить фотографию"
        

    def __str__(self):
        return str(self.title)


class Video(models.Model):
    title = models.CharField('Название', max_length=255, blank=True)
    url = models.URLField(null=True, blank=True)
    is_active = models.BooleanField("Активный", default=True)
    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)

    def __str__(self):
        return str(self.title)


    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Добавить видео'