# Generated by Django 2.1.3 on 2018-11-22 12:03

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AverageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latency', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('download_speed', models.DecimalField(decimal_places=1, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('upload_speed', models.DecimalField(decimal_places=1, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='StudyRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3)),
                ('occupation', models.PositiveIntegerField()),
                ('noise', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3)),
                ('humidity', models.DecimalField(decimal_places=1, max_digits=3)),
                ('precipitation', models.DecimalField(decimal_places=1, max_digits=4, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('wind_speed', models.DecimalField(decimal_places=1, max_digits=4, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('wind_direction', models.CharField(max_length=2)),
                ('UV_rays', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(11)])),
                ('solar_intensity', models.DecimalField(decimal_places=1, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('pressure', models.DecimalField(decimal_places=1, max_digits=4, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='averagedata',
            name='network',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='averageData.Network'),
        ),
        migrations.AddField(
            model_name='averagedata',
            name='parking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='averageData.Parking'),
        ),
        migrations.AddField(
            model_name='averagedata',
            name='studyroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='averageData.StudyRoom'),
        ),
        migrations.AddField(
            model_name='averagedata',
            name='weather',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='averageData.Weather'),
        ),
    ]
