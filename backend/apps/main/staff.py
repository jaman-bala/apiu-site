from django.db import models

class Staff(models.Model):
    photo = models.ImageField('Добавить фото', upload_to='photo', blank=True)
    title = models.CharField('Ф.И.О', max_length=255, blank=True)
    position = models.CharField('Должность', max_length=255, blank=True)
    phone = models.CharField('Телефон', max_length=255, blank=True)
    email = models.EmailField('Почта', max_length=255, blank=True)
    kab = models.CharField('Кабинет', max_length=255, blank=True)
    is_active = models.BooleanField("Активный", default=True)
    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)
    
    

    def __str__(self):
        return str(self.title)


    class Meta:
        verbose_name = 'Списиок сотрудников'
        verbose_name_plural = 'Таблица сотрудников'