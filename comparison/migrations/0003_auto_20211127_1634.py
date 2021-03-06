# Generated by Django 3.2.9 on 2021-11-27 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0007_alter_documents_realstatetype'),
        ('comparison', '0002_residentbuilding'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='residentbuilding',
            name='area',
        ),
        migrations.AddField(
            model_name='residentbuilding',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='residentbuilding',
            name='document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='office.documents'),
        ),
        migrations.AddField(
            model_name='residentbuilding',
            name='streetCount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='residentdocument',
            name='document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='office.documents'),
        ),
        migrations.CreateModel(
            name='CompareBuilding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compareDate', models.DateField(blank=True, null=True)),
                ('CompareareaNumber', models.IntegerField(blank=True, null=True)),
                ('Comparearea', models.IntegerField(blank=True, null=True)),
                ('buildingValue', models.IntegerField(blank=True, null=True)),
                ('priceMeter', models.IntegerField(blank=True, null=True)),
                ('ComparestreetCount', models.IntegerField(blank=True, null=True)),
                ('CompareareaUsage', models.SmallIntegerField(blank=True, choices=[(1, 'سكنى'), (2, 'تجارى'), (3, 'مكتبى')], null=True)),
                ('Compareaddress', models.CharField(blank=True, max_length=255, null=True)),
                ('CompareareaLevel', models.SmallIntegerField(blank=True, choices=[(1, 'عالى'), (2, 'متوسط'), (3, 'منخفض')], null=True)),
                ('residentBuilding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comparison.residentbuilding')),
            ],
        ),
    ]
