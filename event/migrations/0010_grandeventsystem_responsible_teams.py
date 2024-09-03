# Generated by Django 5.0.6 on 2024-08-07 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_grandeventparticipant'),
        ('teams', '0002_alter_awsteams_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='grandeventsystem',
            name='responsible_teams',
            field=models.ManyToManyField(help_text='Responsible teams for the events', related_name='teams', to='teams.awsteams'),
        ),
    ]
