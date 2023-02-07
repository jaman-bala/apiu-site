from django.db import models


class Create(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    email = models.EmailField("Почта")
    city = models.CharField("Адрес", max_length=200)
    phone = models.CharField("Номер телефона", max_length=16)
    title = models.CharField("Вопрос", max_length=200)
    text = models.TextField("Описание")
    file = models.FileField(upload_to='file', blank=True, null=True)
    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)


    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Онлайн заявка'
        verbose_name_plural = 'Онлайн заявки'    
