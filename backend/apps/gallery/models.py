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
