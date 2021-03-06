# Generated by Django 3.0 on 2022-02-01 16:12

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('comparison', '0011_auto_20220201_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='comparebuilding',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='Compareaddress'),
        ),
        migrations.AddField(
            model_name='damagedbuildingrate',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='normalAge'),
        ),
        migrations.AddField(
            model_name='directbuildingcost',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='areaBuildCost'),
        ),
        migrations.AddField(
            model_name='residentbuilding',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='address'),
        ),
        migrations.AddField(
            model_name='residentdocument',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='residentRate'),
        ),
        migrations.AddField(
            model_name='undirectbuildingcost',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='technicalFees'),
        ),
    ]
