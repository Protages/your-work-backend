# Generated by Django 4.1.7 on 2023-02-24 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
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
