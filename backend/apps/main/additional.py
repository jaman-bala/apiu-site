from django.db import models

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
