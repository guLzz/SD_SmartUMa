# Generated by Django 2.1.3 on 2018-11-28 15:46

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('averageData', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='network',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='parking',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='studyroom',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='UV_rays',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='precipitation',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='pressure',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='averagedata',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='network',
            name='latency',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='weather',
            name='humidity',
            field=models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='weather',
            name='wind_direction',
            field=models.CharField(choices=[('N', 'North'), ('S', 'South'), ('E', 'East'), ('w', 'West'), ('NW', 'Northwest'), ('NE', 'Northeast'), ('SW', 'Southwest'), ('SE', 'Southeast')], default='N', max_length=2),
        ),
    ]
