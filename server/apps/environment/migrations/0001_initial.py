# Generated by Django 3.2.15 on 2022-11-04 10:29

import apps.environment.models.rooms
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(40)], verbose_name='classes delegated to this subject')),
            ],
        ),
        migrations.CreateModel(
            name='AvalilableOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='preset title')),
            ],
            options={
                'verbose_name_plural': 'available options',
            },
        ),
        migrations.CreateModel(
            name='GenerationSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='name of settings')),
                ('blocks_must_align', models.BooleanField(default=False)),
                ('max_subjects_per_block', models.PositiveIntegerField(default=12, validators=[django.core.validators.MaxValueValidator(30)])),
                ('blocks', models.PositiveIntegerField(default=4, validators=[django.core.validators.MaxValueValidator(12)], verbose_name='number of option blocks')),
                ('class_size', models.PositiveIntegerField(default=24, validators=[django.core.validators.MaxValueValidator(40)], verbose_name='max class size')),
                ('lesson_cost', models.FloatField(default=5000, verbose_name='cost per lesson')),
            ],
            options={
                'verbose_name_plural': 'Settings',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=apps.environment.models.rooms.generate_room_code, max_length=8, verbose_name='room code')),
                ('domain', models.CharField(max_length=40, verbose_name='domain name')),
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('public', models.BooleanField(default=False, verbose_name='room is public')),
            ],
        ),
    ]
