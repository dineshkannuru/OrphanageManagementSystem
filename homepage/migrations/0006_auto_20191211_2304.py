# Generated by Django 2.1.2 on 2019-12-11 17:34

import datetime
from django.db import migrations, models
import django.utils.timezone
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20191211_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=homepage.models.user_image_upload_url),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='verification',
            name='hit',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 23, 3, 23, 359526)),
        ),
    ]