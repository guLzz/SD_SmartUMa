# Generated by Django 2.1.3 on 2018-11-30 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudyRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3)),
                ('occupation', models.PositiveIntegerField()),
                ('noise', models.PositiveIntegerField()),
                ('room', models.CharField(choices=[('0', 'Ground Floor'), ('1', '1st Floor'), ('2', '2nd Floor'), ('2-PC', 'Computer Room'), ('3', 'Library')], default='0', max_length=4)),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
