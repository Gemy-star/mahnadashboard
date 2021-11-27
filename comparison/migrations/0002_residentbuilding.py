# Generated by Django 3.2.9 on 2021-11-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparison', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResidentBuilding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('residentDate', models.DateField(blank=True, null=True)),
                ('areaNumber', models.IntegerField(blank=True, null=True)),
                ('area', models.IntegerField(blank=True, null=True)),
                ('areaUsage', models.SmallIntegerField(blank=True, choices=[(1, 'سكنى'), (2, 'تجارى'), (3, 'مكتبى')], null=True)),
            ],
        ),
    ]