# Generated by Django 3.2.9 on 2021-11-12 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0002_auto_20211112_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='dateEntered',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 11, 12, 19, 41, 15, 51412)),
        ),
    ]
