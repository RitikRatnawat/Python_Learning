import random
from django.shortcuts import render
from django.http import JsonResponse
from .models import Car


def cars(request):
    car = Car.objects.create(car_name=f"Nexon-{random.randint(0, 100)}", car_type="SUV")
    queryset = Car.objects.all()

    json_data = {"data": [{"name": car.car_name, "type": car.car_type, "speed": car.speed} for car in queryset]}

    return JsonResponse(json_data)
