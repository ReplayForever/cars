from datetime import date
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class OrderCar(models.Model):
    color = models.ForeignKey("Color", related_name="order", on_delete=models.CASCADE)
    type = models.ForeignKey("CarType", related_name="order", on_delete=models.CASCADE)
    order_time = models.DateField(default=date.today)
    count = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(2147483647)]
    )

    def __str__(self) -> str:
        return str(self.id)
