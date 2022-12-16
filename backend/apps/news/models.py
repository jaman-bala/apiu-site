from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=70)
    anons = models.CharField('Анонс', max_length=2500, blank=True, null=True)
    full_text = models.TextField('Статья')
    img = models.ImageField('Добавить фото', upload_to='img', blank=True, null=True)
    specs = models.FileField('Добавить файл', upload_to='specs', blank=True, null=True)
    date = models.DateTimeField('Дата публикации')
    video = models.FileField('Добавить видео', upload_to='videos_uploaded',null=True, blank=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'