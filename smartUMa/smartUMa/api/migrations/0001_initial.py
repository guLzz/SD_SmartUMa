# Generated by Django 2.1.3 on 2018-12-10 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('wind_speed', models.FloatField()),
                ('wind_direction', models.CharField(max_length=2)),
                ('solar_intensity', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
