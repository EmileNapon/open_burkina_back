# Generated by Django 5.1.5 on 2025-02-23 12:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='contractor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestataire', to=settings.AUTH_USER_MODEL),
        ),
    ]
