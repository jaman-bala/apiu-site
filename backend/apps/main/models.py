from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField('Название', max_length=10, blank=True)
    img1 = models.ImageField(upload_to='img', blank=True)
    title1 = models.CharField('Название 1 каруселя', max_length=250, blank=True)
    text1 = models.CharField('Текст 1 каруселя', max_length=250, blank=True)
    img2 = models.ImageField(upload_to='img', blank=True)
    title2 = models.CharField('Название 2 каруселя', max_length=250, blank=True)
    text2 = models.CharField('Текст 2 каруселя', max_length=250, blank=True)
    img3 = models.ImageField(upload_to='img', blank=True)
    title3 = models.CharField('Название 3 каруселя', max_length=250, blank=True)
    text3 = models.CharField('Текст 3 каруселя', max_length=250, blank=True)
    img4 = models.ImageField(upload_to='img', blank=True)
    title4 = models.CharField('Название 4 каруселя', max_length=250, blank=True)
    text4 = models.CharField('Текст 4 каруселя', max_length=250, blank=True)
    img5 = models.ImageField(upload_to='img', blank=True)
    title5 = models.CharField('Название 5 каруселя', max_length=250, blank=True)
    text5 = models.CharField('Текст 5 каруселя', max_length=250, blank=True)
    img6 = models.ImageField(upload_to='img', blank=True) 
    title6 = models.CharField('Название 6 каруселя', max_length=250, blank=True)
    text6 = models.CharField('Текст 6 каруселя', max_length=250, blank=True)
    img7 = models.ImageField(upload_to='img', blank=True) 
    title7 = models.CharField('Название 7 каруселя', max_length=250, blank=True)
    text7 = models.CharField('Текст 7 каруселя', max_length=250, blank=True)
    img8 = models.ImageField(upload_to='img', blank=True) 
    title8 = models.CharField('Название 8 каруселя', max_length=250, blank=True)
    text8 = models.CharField('Текст 8 каруселя', max_length=250, blank=True)
    img9 = models.ImageField(upload_to='img', blank=True) 
    title9 = models.CharField('Название 9 каруселя', max_length=250, blank=True)
    text9 = models.CharField('Текст 9 каруселя', max_length=250, blank=True)
    img10 = models.ImageField(upload_to='img', blank=True)    
    title10 = models.CharField('Название 10 каруселя', max_length=250, blank=True)
    text10 = models.CharField('Текст 10 каруселя', max_length=250, blank=True)
   

    def __str__(self):
        return str(self.title)


    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Добавить фото'