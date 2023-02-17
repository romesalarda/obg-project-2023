# Generated by Django 3.2.15 on 2023-02-07 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('generator', '0001_initial'),
        ('environment', '0002_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='optionblocks',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='option_blocks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='optionblocks',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='environment.room', verbose_name='room connected to'),
        ),
        migrations.AddField(
            model_name='inserttogether',
            name='settings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='environment.generationsettings', verbose_name='settings connected to'),
        ),
        migrations.AddField(
            model_name='inserttogether',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targets', to='students.option', verbose_name='target option'),
        ),
        migrations.AddField(
            model_name='inserttogether',
            name='targets',
            field=models.ManyToManyField(to='students.Option', verbose_name='target subjects'),
        ),
        migrations.AddField(
            model_name='block',
            name='blocks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to='generator.optionblocks', verbose_name='set of blocks connected to'),
        ),
        migrations.AddField(
            model_name='block',
            name='options',
            field=models.ManyToManyField(related_name='options', to='students.Option', verbose_name='options connected to the block'),
        ),
        migrations.AlterUniqueTogether(
            name='optionblocks',
            unique_together={('room', 'title')},
        ),
    ]