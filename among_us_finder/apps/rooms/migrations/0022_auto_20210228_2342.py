# Generated by Django 2.2.17 on 2021-02-28 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0021_auto_20210223_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='comment',
            field=models.TextField(),
        ),
    ]