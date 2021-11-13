# Generated by Django 3.2.9 on 2021-11-13 11:31

from django.db import migrations, models
import django.db.models.deletion
import office.models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0004_alter_documents_dateentered'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LocationUrl', models.URLField(blank=True, null=True)),
                ('locationDescription', models.TextField(blank=True, null=True)),
                ('locationState', models.SmallIntegerField(choices=[(1, 'ممتازة'), (2, 'جيده'), (3, 'سيئة')], null=True)),
                ('locationLevel', models.SmallIntegerField(choices=[(1, 'مرتفع'), (2, 'منخفض')], null=True)),
                ('FinishType', models.SmallIntegerField(choices=[(1, 'بدون عظم'), (2, 'نصف تشطيب'), (3, ' تشطيب كامل')], null=True)),
                ('structureType', models.SmallIntegerField(choices=[(1, 'خرسانه مسلحة '), (2, ' هيكل معدنى')], null=True)),
                ('locationAge', models.SmallIntegerField(blank=True, null=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.documents')),
            ],
        ),
        migrations.CreateModel(
            name='LocationImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=office.models.get_image_filename, verbose_name='Image')),
                ('location', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='office.preview')),
            ],
        ),
    ]
