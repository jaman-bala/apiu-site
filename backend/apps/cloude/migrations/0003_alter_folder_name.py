# Generated by Django 4.1.3 on 2023-01-26 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloude', '0002_alter_folder_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
