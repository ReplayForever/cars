from django.contrib import admin

from .models import Color, Car, ModelCar, OrderCar

admin.site.register(Color)
admin.site.register(Car)
admin.site.register(ModelCar)
admin.site.register(OrderCar)
