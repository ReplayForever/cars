from django.contrib import admin

from .models import Color, Brand, CarType, OrderCar

admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(CarType)
admin.site.register(OrderCar)
