# Generated by Django 4.1.3 on 2022-12-16 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_remove_articles_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos_uploaded'),
        ),
    ]