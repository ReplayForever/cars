from rest_framework import serializers
from car_app.models import OrderCar
from car_app.serializers.car_type import CarTypeSerializer


class OrderCarSerializer(serializers.ModelSerializer):
    color = serializers.CharField(read_only=True)
    color_id = serializers.IntegerField()
    type = CarTypeSerializer(read_only=True)
    type_id = serializers.IntegerField()

    class Meta:
        model = OrderCar
        fields = ("color", "color_id", "type", "type_id", "count", "order_time")
