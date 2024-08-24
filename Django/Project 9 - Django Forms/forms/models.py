from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.name
