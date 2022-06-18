from rest_framework import serializers
from car_app.models import OrderCar


class OrderCarSerializer(serializers.ModelSerializer):
    color = serializers.CharField(read_only=True)
    color_id = serializers.IntegerField(write_only=True)
    type = serializers.CharField(read_only=True)
    type_id = serializers.IntegerField(write_only=True)
    brand = serializers.PrimaryKeyRelatedField(read_only=True, source='type.brand.name')

    class Meta:
        model = OrderCar
        fields = ("color", "color_id", "type", "type_id", "brand", "count", "order_time")
