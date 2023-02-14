# Generated by Django 4.1.3 on 2023-02-14 08:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0005_vacancy_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='other',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='other',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
        migrations.AddField(
            model_name='tender',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
    ]
