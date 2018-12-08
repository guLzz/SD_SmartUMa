from django.db import models

# Create your models here.
class Weather(models.Model):
	temperature = models.FloatField()
	humidity = models.FloatField()
	wind_speed = models.FloatField()
	wind_direction = models.CharField(max_length=2)
	solar_intensity = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add=True)


def __str__(self):
        return '%f %f %f %s %f' % (self.temperature, self.humidity, self.wind_speed, self.wind_direction, self.solar_intensity)