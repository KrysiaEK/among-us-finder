# Generated by Django 2.2.17 on 2021-01-11 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20210111_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
