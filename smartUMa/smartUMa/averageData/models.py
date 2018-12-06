from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import datetime


class AverageData(models.Model):
    network = models.ForeignKey('Network', on_delete=models.CASCADE)
    parking = models.ForeignKey('Parking', on_delete=models.CASCADE)
    studyroom = models.ForeignKey('StudyRoom', on_delete=models.CASCADE)
    weather = models.ForeignKey('Weather', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(
        default=datetime.now,
        blank=True
    )


class Weather(models.Model):
    temperature = models.DecimalField(
        decimal_places=1,
        max_digits=3
    )  # ºC

    humidity = models.DecimalField(
        validators=[MinValueValidator(0.0)],
        decimal_places=1,
        max_digits=3
    )  # %

    wind_speed = models.DecimalField(
        validators=[MinValueValidator(0.0)],
        decimal_places=1,
        max_digits=4
    )  # m/s

    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "w"
    NORTHWEST = "NW"
    NORTHEAST = "NE"
    SOUTHWEST = "SW"
    SOUTHEAST = "SE"

    wind_direction_choices = (
        (NORTH, 'North'),
        (SOUTH, 'South'),
        (EAST, 'East'),
        (WEST, 'West'),
        (NORTHWEST, 'Northwest'),
        (NORTHEAST, 'Northeast'),
        (SOUTHWEST, 'Southwest'),
        (SOUTHEAST, 'Southeast')
    )

    wind_direction = models.CharField(
        max_length=2,
        choices=wind_direction_choices,
        default=NORTH
    )  # N, S, E, W, NW, NE, SW, SE

    solar_intensity = models.DecimalField(
        validators=[MinValueValidator(0.0)],
        decimal_places=1,
        max_digits=5
    )  # W/m^2


class StudyRoom(models.Model):
    studyroom0 = models.ForeignKey('Floor0', on_delete=models.CASCADE, default=-1)
    studyroom1 = models.ForeignKey('Floor1', on_delete=models.CASCADE, default=-1)
    studyroom2 = models.ForeignKey('Floor2', on_delete=models.CASCADE, default=-1)
    studyroom2PC = models.ForeignKey('Floor2PC', on_delete=models.CASCADE, default=-1)
    studyroom3 = models.ForeignKey('Floor3', on_delete=models.CASCADE, default=-1)


class Floor0(models.Model):
    temperature = models.DecimalField(
        decimal_places=1,
        max_digits=3
    )  # ºC

    occupation = models.PositiveIntegerField()  # 0 <

    noise = models.PositiveIntegerField()  # dB


class Floor1(models.Model):
    temperature = models.DecimalField(
        decimal_places=1,
        max_digits=3
    )  # ºC

    occupation = models.PositiveIntegerField()  # 0 <

    noise = models.PositiveIntegerField()  # dB


class Floor2(models.Model):
    temperature = models.DecimalField(
        decimal_places=1,
        max_digits=3
    )  # ºC

    occupation = models.PositiveIntegerField()  # 0 <

    noise = models.PositiveIntegerField()  # dB


class Floor2PC(models.Model):
    temperature = models.DecimalField(
        decimal_places=1,
        max_digits=3
    )  # ºC

    occupation = models.PositiveIntegerField()  # 0 <

    noise = models.PositiveIntegerField()  # dB


class Floor3(models.Model):
    temperature = models.DecimalField(
        decimal_places=1,
        max_digits=3
    )  # ºC

    occupation = models.PositiveIntegerField()  # 0 <

    noise = models.PositiveIntegerField()  # dB


class Parking(models.Model):
    occupation = models.PositiveIntegerField()  # 0 <


class Network(models.Model):
    latency = models.PositiveIntegerField()  # ms

    download_speed = models.DecimalField(
        validators=[MinValueValidator(0.0)],
        decimal_places=1,
        max_digits=5
    )  # Mbps

    upload_speed = models.DecimalField(
        validators=[MinValueValidator(0.0)],
        decimal_places=1,
        max_digits=5
    )  # Mbps
