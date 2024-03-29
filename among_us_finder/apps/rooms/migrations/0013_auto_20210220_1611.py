# Generated by Django 2.2.17 on 2021-02-20 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0012_message_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='rooms.Room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='map',
            field=models.PositiveSmallIntegerField(choices=[(1, 'The Skeld'), (2, 'Polus'), (3, 'MiraHQ'), (4, 'The Airship')]),
        ),
    ]
