from django.db import models

class Create(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    email = models.EmailField("Почта")
    phone = models.IntegerField("Номер телефона")
    title = models.CharField("Название", max_length=50)
    text = models.TextField("Описание")
    file = models.FileField(upload_to='file', blank=True, null=True)
    date = models.DateTimeField("Дата публикации")


    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Онлайн заявка'
        verbose_name_plural = 'Онлайн заявки'    
