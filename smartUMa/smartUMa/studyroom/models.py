from datetime import datetime

from django.db import models


class StudyRoom(models.Model):
    temperature = models.DecimalField(
        decimal_places=1,
        max_digits=3
    )  # ºC

    occupation = models.PositiveIntegerField()  # 0 <

    noise = models.PositiveIntegerField()  # dB

    GROUND = "0"
    FIRST = "1"
    SECOND = "2"
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

    timestamp = models.DateTimeField(
        default=datetime.now,
        blank=True
    )



