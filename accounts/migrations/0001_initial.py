# Generated by Django 3.2.9 on 2021-11-12 11:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('is_admin', models.BooleanField(default=False, help_text='Designates whether this user should be treated as an Admin. ', verbose_name='Admin')),
                ('is_accountant', models.BooleanField(default=False, help_text='Designates whether this user should be treated as an Accountant Employee. ', verbose_name='Accountant Employee')),
                ('is_manager', models.BooleanField(default=False, help_text='Designates whether this user should be treated as an Manager Employee. ', verbose_name='Manager Employee ')),
                ('is_resident', models.BooleanField(default=False, help_text='Designates whether this user should be treated as an Resident Employee. ', verbose_name='Resident Employee ')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'أدمن'), (2, 'مدير تنفيذى'), (3, 'محاسب'), (4, 'مقيم')], help_text='User Role in A system ', null=True, verbose_name='User Type')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
