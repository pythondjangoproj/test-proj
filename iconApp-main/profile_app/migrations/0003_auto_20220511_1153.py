# Generated by Django 3.2.12 on 2022-05-11 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0002_usergame'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usergame',
            old_name='game',
            new_name='game_id',
        ),
        migrations.RenameField(
            model_name='userplatform',
            old_name='platforms',
            new_name='platforms_id',
        ),
    ]
