# Generated by Django 3.2.12 on 2022-05-11 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0003_auto_20220511_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usergame',
            old_name='game_id',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='userplatform',
            old_name='platforms_id',
            new_name='platforms',
        ),
    ]