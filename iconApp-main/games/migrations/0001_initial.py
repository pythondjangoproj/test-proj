# Generated by Django 3.2.12 on 2022-04-30 10:03

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('display_name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='full_name', unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('short_name', models.CharField(max_length=50)),
                ('display_image', models.ImageField(blank=True, null=True, upload_to='game_logos')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('updated_by', models.EmailField(max_length=254)),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('object_id', models.CharField(blank=True, max_length=150, null=True)),
                ('name', models.CharField(max_length=255)),
                ('closed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('updated_by', models.EmailField(max_length=254)),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('object_id', models.CharField(blank=True, max_length=150, null=True)),
                ('number', models.PositiveSmallIntegerField()),
                ('scheduled_datetime', models.DateTimeField(blank=True, null=True)),
                ('start_datetime', models.DateTimeField(blank=True, null=True)),
                ('end_datetime', models.DateTimeField(blank=True, null=True)),
                ('ext_report_status', models.CharField(choices=[('REP', 'Report'), ('DIS', 'Dispute')], default='REP', max_length=3)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.group')),
            ],
            options={
                'verbose_name_plural': 'Matches',
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StageType',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('updated_by', models.EmailField(max_length=254)),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('object_id', models.CharField(blank=True, max_length=150, null=True)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='full_name', unique_with=('scheduled_date_start',))),
                ('size', models.PositiveSmallIntegerField()),
                ('scheduled_date_start', models.DateField()),
                ('scheduled_date_end', models.DateField()),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='games.game')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('updated_by', models.EmailField(max_length=254)),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('object_id', models.CharField(blank=True, max_length=150, null=True)),
                ('name', models.CharField(max_length=255)),
                ('number', models.PositiveSmallIntegerField()),
                ('is_closed', models.BooleanField(default=False)),
                ('stage_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='games.stagetype')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.tournament')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('updated_by', models.EmailField(max_length=254)),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('object_id', models.CharField(blank=True, max_length=150, null=True)),
                ('number', models.PositiveSmallIntegerField()),
                ('start_datetime', models.DateTimeField(blank=True, null=True)),
                ('end_datetime', models.DateTimeField(blank=True, null=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.group')),
                ('stage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.stage')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.tournament')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MatchParticipant',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('object_id', models.CharField(blank=True, max_length=150, null=True)),
                ('checked_in_at', models.DateTimeField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.match')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.tournament')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='match',
            name='round',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.round'),
        ),
        migrations.AddField(
            model_name='match',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.stage'),
        ),
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.tournament'),
        ),
        migrations.AddField(
            model_name='group',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.tournament'),
        ),
        migrations.AddField(
            model_name='game',
            name='platforms',
            field=models.ManyToManyField(to='games.Platform'),
        ),
    ]