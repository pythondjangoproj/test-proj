# Generated by Django 3.2.12 on 2022-05-10 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_delete_completeprofile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=255)),
                ('display_image', models.ImageField(blank=True, default='default-avatar.png', null=True, upload_to='')),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='games.game')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
