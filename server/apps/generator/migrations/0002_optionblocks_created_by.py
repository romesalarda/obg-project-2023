# Generated by Django 3.2.15 on 2022-12-30 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='optionblocks',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='option_blocks', to=settings.AUTH_USER_MODEL),
        ),
    ]
