# Generated by Django 4.1.3 on 2022-12-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloude', '0003_info_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos_uploaded'),
        ),
    ]
