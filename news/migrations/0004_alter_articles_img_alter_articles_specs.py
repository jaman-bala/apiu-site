# Generated by Django 4.1.3 on 2022-11-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_articles_img_alter_articles_specs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='specs',
            field=models.FileField(blank=True, null=True, upload_to='specs'),
        ),
    ]
