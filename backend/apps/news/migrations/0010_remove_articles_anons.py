# Generated by Django 4.1.3 on 2022-12-22 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_articles_img_alter_articles_specs_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='anons',
        ),
    ]
