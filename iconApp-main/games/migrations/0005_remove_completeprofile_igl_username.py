# Generated by Django 3.2.12 on 2022-05-06 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_completeprofile_igl_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completeprofile',
            name='IGL_Username',
        ),
    ]
