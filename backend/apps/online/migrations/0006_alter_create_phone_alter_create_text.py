# Generated by Django 4.1.3 on 2023-01-17 11:14

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0005_alter_create_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create',
            name='phone',
            field=phone_field.models.PhoneField(help_text='Contact phone number', max_length=16, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='create',
            name='text',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
