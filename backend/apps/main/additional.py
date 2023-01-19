from django.db import models

class Info(models.Model):
    title = models.CharField('Название', max_length=200, blank=True)
    video = models.URLField(null=True, blank=True)
    

    def __str__(self):
        return str(self.title)


    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Добавить видео'
