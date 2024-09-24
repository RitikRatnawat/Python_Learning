from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=70)
    roll_number = models.IntegerField()
    city = models.CharField(max_length=70)

    def __str__(self):
        return self.name