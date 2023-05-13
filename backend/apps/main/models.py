from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField('Название Каруселя', max_length=55)
    img1 = models.ImageField('Фотография', upload_to='img', blank=True)
    
    is_active = models.BooleanField("Активный", default=True)
    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)

    def __str__(self):
        return str(self.title)


    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Добавить фото'