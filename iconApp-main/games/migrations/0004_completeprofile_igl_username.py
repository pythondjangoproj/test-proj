# Generated by Django 3.2.12 on 2022-05-06 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_remove_match_ext_report_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='completeprofile',
            name='IGL_Username',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
