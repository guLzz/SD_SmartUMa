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
    temperature = models.DecimalField(
        decimal_places=1,
        max_digits=3
    )  # ºC

    occupation = models.PositiveIntegerField()  # 0 <

    noise = models.PositiveIntegerField()  # dB

    GROUND = "0"
    FIRST = " 1"
    SECOND = " 2"
    COMPUTER = "2-PC"
    LIBRARY = "3"

    room_choices = (
        (GROUND, 'Ground Floor'),
        (FIRST, '1st Floor'),
        (SECOND, '2nd Floor'),
        (COMPUTER, 'Computer Room'),
        (LIBRARY, 'Library')
    )

    room = models.CharField(
        max_length=4,
        choices=room_choices,
        default=GROUND
    )


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
