# Generated by Django 4.1.3 on 2023-01-19 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloude', '0002_alter_file_options_alter_folder_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='files/'),
        ),
    ]
