# Generated by Django 2.2.5 on 2019-10-13 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_player_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='team',
            new_name='team_id',
        ),
    ]
