# Generated by Django 3.2.9 on 2021-11-13 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0005_locationimages_preview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preview',
            old_name='LocationUrl',
            new_name='locationUrl',
        ),
    ]
