from django.db import models

class Category(models.Model):
    name = models.CharField("Название категории", max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Категория проекта"
        verbose_name_plural = "Категории категория"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(verbose_name="Название проекта", max_length=200)
    description = models.TextField(verbose_name="Описание")



class File(models.Model):
    title = models.CharField(verbose_name='Название файла', max_length=50)
    file = models.FileField(upload_to='media', blank=True, verbose_name="Добавить файл") 
    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)


    class Meta:
        verbose_name = "Добавить"
        verbose_name_plural = "Добавить файл"
        

    def __str__(self):
        return str(self.title)
