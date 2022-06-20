from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self) -> str:
        return self.name
