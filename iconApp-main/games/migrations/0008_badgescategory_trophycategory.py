# Generated by Django 3.2.12 on 2022-05-12 13:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_alter_game_display_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrophyCategory',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('updated_by', models.EmailField(max_length=254)),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('object_id', models.CharField(blank=True, max_length=150, null=True)),
                ('category_name', models.CharField(max_length=225)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BadgesCategory',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('updated_by', models.EmailField(max_length=254)),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('object_id', models.CharField(blank=True, max_length=150, null=True)),
                ('badge_type', models.CharField(max_length=225)),
                ('display_name', models.CharField(max_length=225)),
                ('badges_image', models.ImageField(blank=True, null=True, upload_to='badges_logos')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.trophycategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]