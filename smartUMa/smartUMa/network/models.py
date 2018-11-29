from datetime import datetime

from django.core.validators import MinValueValidator
from django.db import models


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

    timestamp = models.DateTimeField(
        default=datetime.now,
        blank=True
    )


