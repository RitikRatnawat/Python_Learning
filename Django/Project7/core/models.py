from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name


@receiver(post_save, sender=Car)
def get_speed(sender, instance, **kwargs):
    print(f"Car Object {instance.car_name} Created")
    print(sender)
    print(kwargs)


"""
Types of Signals : 
1. pre_save
2. post_save
3. pre_delete
4. post_delete
"""