from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    speed = models.IntegerField(default=60)

    def __str__(self):
        return self.name