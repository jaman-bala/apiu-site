from django.db import models



class Library(models.Model):
    image = models.ImageField(verbose_name="Обложка", upload_to="files", null=True, blank=True)
    title = models.CharField(verbose_name='Наименование', max_length=50)
    author = models.CharField(verbose_name="Автор", max_length=50)
    books = models.FileField(upload_to='files', blank=True, verbose_name="Добавить файл") 



    class Meta:
        verbose_name = "Добавить"
        verbose_name_plural = "Добавить книги"
        

    def __str__(self):
        return str(self.title)
