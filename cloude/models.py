from django.db import models

class Photo(models.Model):
    title = models.CharField('Название', max_length=10, blank=True)
    img1 = models.ImageField(upload_to='img', blank=True)
    img2 = models.ImageField(upload_to='img', blank=True)
    img3 = models.ImageField(upload_to='img', blank=True)

    def __str__(self):
        return str(self.id)


    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Добавить фото'


