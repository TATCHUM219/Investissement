# Generated by Django 5.0.7 on 2024-08-01 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_machine_image_alter_client_date_inscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date_inscription',
            field=models.DateField(default=datetime.datetime(2024, 8, 1, 16, 32, 41, 168224, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='public'),
        ),
    ]
