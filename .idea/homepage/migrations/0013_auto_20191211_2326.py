# Generated by Django 2.2.5 on 2019-12-11 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_auto_20191211_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='hit',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 23, 26, 31, 65318)),
        ),
    ]