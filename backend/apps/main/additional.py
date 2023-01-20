from django.db import models

class Video(models.Model):
    title = models.CharField('Название', max_length=255, blank=True)
    url = models.URLField(null=True, blank=True)
    

    def __str__(self):
        return str(self.title)


    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Добавить видео'
