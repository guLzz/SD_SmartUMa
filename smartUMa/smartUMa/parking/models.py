from datetime import datetime

from django.db import models


class Parking(models.Model):
    occupation = models.PositiveIntegerField()  # 0 <

    timestamp = models.DateTimeField(
        default=datetime.now,
        blank=True
    )
