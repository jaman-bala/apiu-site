# Generated by Django 4.1.3 on 2022-12-16 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_articles_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='anons',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Анонс'),
        ),
    ]
