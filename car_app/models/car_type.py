from django.db import models


class CarType(models.Model):
    name = models.CharField(max_length=32, unique=True)
    brand = models.ForeignKey("Brand", related_name="cartype", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
