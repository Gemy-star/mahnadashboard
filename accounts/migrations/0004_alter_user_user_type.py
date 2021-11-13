# Generated by Django 3.2.9 on 2021-11-13 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211113_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'أدمن'), (2, 'مدير تنفيذى'), (3, 'محاسب'), (4, 'مقيم'), (5, 'مدخل بيانات'), (6, 'معاين ')], help_text='User Role in A system ', null=True, verbose_name='User Type'),
        ),
    ]
