# Generated by Django 4.1.7 on 2023-02-26 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('candidate', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='app.candidate', verbose_name='candidate')),
                ('company', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='app.company', verbose_name='company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissions', models.CharField(blank=True, max_length=128, null=True, verbose_name='permissions')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='app.company', verbose_name='company')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workplace', to=settings.AUTH_USER_MODEL, verbose_name='employee')),
            ],
        ),
    ]
