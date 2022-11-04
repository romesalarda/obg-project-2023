# Generated by Django 3.2.15 on 2022-11-04 10:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_requirement_grade'),
        ('environment', '0004_auto_20221103_1659'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='generationsettings',
            unique_together={('room', 'title')},
        ),
        migrations.CreateModel(
            name='AvailableOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(40)], verbose_name='classes delegated to this subject')),
                ('available_options', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='environment.avalilableoptions', verbose_name='available options')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.option', verbose_name='option connected to')),
            ],
        ),
    ]
