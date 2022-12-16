from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=70)
    anons = models.CharField('Анонс', max_length=250, blank=True, null=True)
    full_text = models.TextField('Статья')
    img = models.ImageField(upload_to='img', blank=True, null=True)
    specs = models.FileField(upload_to='specs', blank=True, null=True)
    date = models.DateTimeField('Дата публикации')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'