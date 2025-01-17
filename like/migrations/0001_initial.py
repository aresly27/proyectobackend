# Generated by Django 5.0.6 on 2024-06-30 04:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logro', '0003_logro_public'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('status', models.BooleanField(default=True, verbose_name='Estatus')),
                ('logro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logro.logro', verbose_name='logro')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user_id')),
            ],
            options={
                'db_table': 'like',
            },
        ),
    ]
