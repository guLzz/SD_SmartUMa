from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


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
    WEST = "W"
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

    timestamp = models.DateTimeField(
        default=datetime.now,
        blank=True
    )


