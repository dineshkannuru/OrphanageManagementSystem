# Generated by Django 2.1.2 on 2019-12-11 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20191211_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='hit',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 21, 55, 16, 835264)),
        ),
    ]
