from django.db import models




class Library(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=50)
    author = models.CharField(verbose_name="Автор", max_length=50)
    books = models.FileField(upload_to='media', blank=True, verbose_name="Добавить файл") 



    class Meta:
        verbose_name = "Добавить"
        verbose_name_plural = "Добавить файл"
        

    def __str__(self):
        return str(self.title)
