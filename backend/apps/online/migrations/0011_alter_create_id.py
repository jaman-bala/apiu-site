# Generated by Django 4.1.3 on 2023-01-19 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0010_merge_0003_auto_20230108_1216_0009_alter_create_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
