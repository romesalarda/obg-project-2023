# Generated by Django 3.2.15 on 2022-12-30 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_optionblocks_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='optionblocks',
            name='completed_nodes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='optionblocks',
            name='generated_nodes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='optionblocks',
            name='generation_time',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='optionblocks',
            name='success_percentage',
            field=models.FloatField(default=0),
        ),
    ]
