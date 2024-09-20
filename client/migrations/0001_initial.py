# Generated by Django 5.0.6 on 2024-07-24 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('date_inscription', models.DateTimeField()),
                ('solde_depot', models.IntegerField()),
                ('solde_a_retirer', models.IntegerField()),
                ('parain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='client.client')),
            ],
        ),
        migrations.CreateModel(
            name='Depot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_heure', models.DateTimeField()),
                ('montant', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('montant', models.IntegerField()),
                ('periode_minage', models.IntegerField()),
                ('montant_a_miner', models.IntegerField()),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='client.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Achat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_heure', models.DateTimeField()),
                ('solde_miner', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='client.machine')),
            ],
        ),
        migrations.CreateModel(
            name='Minage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_heure', models.DateTimeField()),
                ('montant', models.IntegerField()),
                ('achat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='client.achat')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
        migrations.CreateModel(
            name='Retrait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_heure', models.DateTimeField()),
                ('montant', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
    ]
