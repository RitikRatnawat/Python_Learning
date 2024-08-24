from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
