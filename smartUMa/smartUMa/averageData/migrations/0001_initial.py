# Generated by Django 2.1.4 on 2018-12-08 09:31

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
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Floor0',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3)),
                ('occupation', models.PositiveIntegerField()),
                ('noise', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Floor1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3)),
                ('occupation', models.PositiveIntegerField()),
                ('noise', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Floor2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3)),
                ('occupation', models.PositiveIntegerField()),
                ('noise', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Floor2PC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3)),
                ('occupation', models.PositiveIntegerField()),
                ('noise', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Floor3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3)),
                ('occupation', models.PositiveIntegerField()),
                ('noise', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latency', models.PositiveIntegerField()),
                ('download_speed', models.DecimalField(decimal_places=1, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('upload_speed', models.DecimalField(decimal_places=1, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudyRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studyroom0', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='averageData.Floor0')),
                ('studyroom1', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='averageData.Floor1')),
                ('studyroom2', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='averageData.Floor2')),
                ('studyroom2PC', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='averageData.Floor2PC')),
                ('studyroom3', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='averageData.Floor3')),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3)),
                ('humidity', models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('wind_speed', models.DecimalField(decimal_places=1, max_digits=4, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('wind_direction', models.CharField(choices=[('N', 'North'), ('S', 'South'), ('E', 'East'), ('w', 'West'), ('NW', 'Northwest'), ('NE', 'Northeast'), ('SW', 'Southwest'), ('SE', 'Southeast')], default='N', max_length=2)),
                ('solar_intensity', models.DecimalField(decimal_places=1, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0)])),
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
