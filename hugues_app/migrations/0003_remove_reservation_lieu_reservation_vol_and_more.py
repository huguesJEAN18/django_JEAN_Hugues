# Generated by Django 4.1.7 on 2024-03-01 10:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hugues_app', '0002_vol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='lieu',
        ),
        migrations.AddField(
            model_name='reservation',
            name='vol',
            field=models.ForeignKey(default=datetime.datetime(2024, 3, 1, 10, 12, 15, 415966, tzinfo=datetime.timezone.utc), on_delete=django.db.models.deletion.CASCADE, to='hugues_app.vol'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_reservation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
