from django.db import models


class CarType(models.Model):
    type = models.CharField(max_length=32, unique=True)
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)

    def __str__(self):
        return self.type