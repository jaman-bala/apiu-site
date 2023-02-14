from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField('Название Каруселя', max_length=10)
    img1 = models.ImageField('Фотография №1', upload_to='img', blank=True)
    title1 = models.CharField('Название 1 каруселя', max_length=250, blank=True)
    text1 = models.CharField('Текст 1 каруселя', max_length=250, blank=True)
    img2 = models.ImageField('Фотография №2', upload_to='img', blank=True)
    title2 = models.CharField('Название 2 каруселя', max_length=250, blank=True)
    text2 = models.CharField('Текст 2 каруселя', max_length=250, blank=True)
    img3 = models.ImageField('Фотография №3', upload_to='img', blank=True)
    title3 = models.CharField('Название 3 каруселя', max_length=250, blank=True)
    text3 = models.CharField('Текст 3 каруселя', max_length=250, blank=True)
    img4 = models.ImageField('Фотография №4', upload_to='img', blank=True)
    title4 = models.CharField('Название 4 каруселя', max_length=250, blank=True)
    text4 = models.CharField('Текст 4 каруселя', max_length=250, blank=True)
    img5 = models.ImageField('Фотография №5', upload_to='img', blank=True)
    title5 = models.CharField('Название 5 каруселя', max_length=250, blank=True)
    text5 = models.CharField('Текст 5 каруселя', max_length=250, blank=True)
    img6 = models.ImageField('Фотография №6', upload_to='img', blank=True) 
    title6 = models.CharField('Название 6 каруселя', max_length=250, blank=True)
    text6 = models.CharField('Текст 6 каруселя', max_length=250, blank=True)
    img7 = models.ImageField('Фотография №7', upload_to='img', blank=True) 
    title7 = models.CharField('Название 7 каруселя', max_length=250, blank=True)
    text7 = models.CharField('Текст 7 каруселя', max_length=250, blank=True)
    img8 = models.ImageField('Фотография №8', upload_to='img', blank=True) 
    title8 = models.CharField('Название 8 каруселя', max_length=250, blank=True)
    text8 = models.CharField('Текст 8 каруселя', max_length=250, blank=True)
    img9 = models.ImageField('Фотография №9', upload_to='img', blank=True) 
    title9 = models.CharField('Название 9 каруселя', max_length=250, blank=True)
    text9 = models.CharField('Текст 9 каруселя', max_length=250, blank=True)
    img10 = models.ImageField('Фотография №10', upload_to='img', blank=True)    
    title10 = models.CharField('Название 10 каруселя', max_length=250, blank=True)
    text10 = models.CharField('Текст 10 каруселя', max_length=250, blank=True)
    is_active = models.BooleanField("Активный", default=True)
    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)

    def __str__(self):
        return str(self.title)


    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Добавить фото'