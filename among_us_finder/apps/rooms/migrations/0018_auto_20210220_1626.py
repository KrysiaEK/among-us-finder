# Generated by Django 2.2.17 on 2021-02-20 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0017_auto_20210220_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='level',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Beginner'), (2, 'Medium'), (3, 'Advanced')]),
        ),
        migrations.AlterField(
            model_name='room',
            name='map',
            field=models.PositiveSmallIntegerField(choices=[('', '----'), (1, 'The Skeld'), (2, 'Polus'), (3, 'MiraHQ'), (4, 'The Airship')]),
        ),
    ]
