# Generated by Django 2.2.5 on 2019-10-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_team_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='name',
            new_name='team_name',
        ),
        migrations.AddField(
            model_name='player',
            name='team_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
