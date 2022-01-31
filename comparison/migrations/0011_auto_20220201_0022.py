# Generated by Django 3.0 on 2022-01-31 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0012_preview_completed'),
        ('comparison', '0010_residentdocument_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='residentdocument',
            name='document',
        ),
        migrations.AddField(
            model_name='residentdocument',
            name='previews',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='office.Preview'),
        ),
    ]
