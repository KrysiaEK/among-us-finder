# Generated by Django 2.2.17 on 2020-12-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_level_of_advancement'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='level_of_advancement',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Beginner'), (2, 'Medium'), (3, 'Advanced')], default=1),
            preserve_default=False,
        ),
    ]
