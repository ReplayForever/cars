from rest_framework import serializers
from car_app.models import OrderCar


class OrderCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCar
        fields = ("color", "type", "count", "order_time")
