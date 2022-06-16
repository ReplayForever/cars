from datetime import date
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Color(models.Model):
    color = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.color


class Car(models.Model):
    car = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.car


class ModelCar(models.Model):
    model_car = models.CharField(max_length=32, unique=True)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)

    def __str__(self):
        return self.model_car


class OrderCar(models.Model):
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    model_car = models.ForeignKey('ModelCar', on_delete=models.CASCADE)
    order_time = models.DateField(default=date.today)
    count = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(2147483647)])

    def __str__(self):
        return str(self.id)
