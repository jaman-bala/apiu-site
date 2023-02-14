from django.db import models


class File(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=50)
    file = models.FileField(upload_to='media', blank=True, verbose_name="Добавить файл") 
    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)


    class Meta:
        verbose_name = "Добавить"
        verbose_name_plural = "Добавить файл"
        

    def __str__(self):
        return str(self.title)
