# Generated by Django 2.2.5 on 2020-03-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_xglookup'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='xg_season',
            field=models.FloatField(default=0.0),
        ),
    ]
