from django.db import models

class Staff(models.Model):
    title = models.CharField('Ф.И.О', max_length=255, blank=True)
    position = models.CharField('Должность', max_length=255, blank=True)
    phone = models.CharField('Телефон', max_length=255, blank=True)
    email = models.EmailField('Почта', max_length=255, blank=True)
    kab = models.CharField('Кабинет', max_length=255, blank=True)
    
    

    def __str__(self):
        return str(self.title)


    class Meta:
        verbose_name = 'Списиок сотрудников'
        verbose_name_plural = 'Таблица сотрудников'