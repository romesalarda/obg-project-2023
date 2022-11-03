# Generated by Django 3.2.15 on 2022-11-03 16:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('environment', '0001_initial'),
        ('students', '0005_alter_requirement_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionBlocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('number_of_blocks', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(15)], verbose_name='number of blocks')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='environment.room', verbose_name='room connected to')),
            ],
        ),
        migrations.CreateModel(
            name='InsertTogether',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='environment.room', verbose_name='')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targets', to='students.option', verbose_name='target option')),
                ('targets', models.ManyToManyField(to='students.Option', verbose_name='target subjects')),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_subjects', models.IntegerField(verbose_name='number of subjects')),
                ('block_id', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(15)], verbose_name='block id')),
                ('blocks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generator.optionblocks', verbose_name='set of blocks connected to')),
                ('options', models.ManyToManyField(to='students.Option', verbose_name='options connected to the block')),
            ],
        ),
    ]
