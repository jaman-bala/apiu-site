# Generated by Django 4.1.3 on 2023-02-14 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0007_alter_tender_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files', verbose_name='Добавить файл'),
        ),
    ]
