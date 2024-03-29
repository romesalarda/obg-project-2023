# Generated by Django 3.2.15 on 2023-02-18 12:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_subjects', models.IntegerField(verbose_name='number of subjects')),
                ('block_id', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(15)], verbose_name='block id')),
            ],
        ),
        migrations.CreateModel(
            name='BlockSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students', models.IntegerField(verbose_name='number of students for this room')),
            ],
        ),
        migrations.CreateModel(
            name='InsertTogether',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Insert together',
            },
        ),
        migrations.CreateModel(
            name='OptionBlocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('number_of_blocks', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(15)], verbose_name='number of blocks')),
                ('success_percentage', models.FloatField(default=0)),
                ('generation_time', models.FloatField(default=0)),
                ('completed_nodes', models.PositiveIntegerField(default=0)),
                ('generated_nodes', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Option blocks',
            },
        ),
    ]
