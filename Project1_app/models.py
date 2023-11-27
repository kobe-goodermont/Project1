from django.db import models


# Create your models here.


class Workout(models.Model):

    TITLE = models.CharField(max_length=200)
    DESCRIPTION = models.CharField(max_length=200)
    CHOICES = (
        ('Chest', 'Chest'),
        ('Arms', 'Arms'),
        ('Legs', 'Legs'),
        ('Back', 'Back'),
        ('Shoulders', 'Shoulders'),

    )
    GROUP = models.CharField(max_length=200, choices=CHOICES)

    def __str__(self):
        return self.TITLE
