# Generated by Django 4.1.7 on 2024-02-29 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hugues_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compagnie', models.CharField(max_length=100)),
                ('numero_vol', models.CharField(max_length=50)),
                ('depart', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('date_depart', models.DateTimeField()),
                ('date_arrivee', models.DateTimeField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
