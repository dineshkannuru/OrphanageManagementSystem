# Generated by Django 2.2.5 on 2019-12-10 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_cateringcompany_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='homepage.CateringCompany'),
        ),
    ]