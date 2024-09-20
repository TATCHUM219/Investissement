# Generated by Django 5.0.7 on 2024-08-03 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_achat_delai_alter_client_date_inscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='achat',
            name='prochain_minage',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 3, 9, 18, 7, 911619, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='achat',
            name='delai',
            field=models.DateField(default=datetime.datetime(2024, 8, 3, 9, 18, 7, 911619, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_inscription',
            field=models.DateField(default=datetime.datetime(2024, 8, 3, 9, 18, 7, 909615, tzinfo=datetime.timezone.utc)),
        ),
    ]
