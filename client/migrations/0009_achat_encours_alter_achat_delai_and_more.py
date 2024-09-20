# Generated by Django 5.0.7 on 2024-08-04 14:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_remove_minage_client_alter_achat_delai_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='achat',
            name='encours',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='achat',
            name='delai',
            field=models.DateField(default=datetime.datetime(2024, 8, 4, 14, 19, 18, 364842, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='achat',
            name='prochain_minage',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 4, 14, 19, 18, 364842, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_inscription',
            field=models.DateField(default=datetime.datetime(2024, 8, 4, 14, 19, 18, 362844, tzinfo=datetime.timezone.utc)),
        ),
    ]
