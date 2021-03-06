# Generated by Django 3.2.9 on 2021-11-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_Entry',
            field=models.BooleanField(default=False, help_text='Designates whether this user should be treated as an Entry Employee ', verbose_name='Entry Employee '),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'أدمن'), (2, 'مدير تنفيذى'), (3, 'محاسب'), (4, 'مقيم'), (5, 'مدخل بيانات')], help_text='User Role in A system ', null=True, verbose_name='User Type'),
        ),
    ]
