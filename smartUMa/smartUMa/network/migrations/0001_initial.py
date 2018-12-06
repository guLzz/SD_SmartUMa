# Generated by Django 2.1.3 on 2018-12-06 17:06

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latency', models.PositiveIntegerField()),
                ('download_speed', models.DecimalField(decimal_places=1, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('upload_speed', models.DecimalField(decimal_places=1, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]