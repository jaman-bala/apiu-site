from django.db import models

class Info(models.Model):
    title = models.CharField('Название', max_length=10, blank=True)
    text = models.TextField('Текст', blank=True)
    photo = models.ImageField(upload_to='img', blank=True)
    video = models.FileField(upload_to='videos_uploaded',null=True, blank=True)
    

    def __str__(self):
        return str(self.id)


    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Добавить информацию'
