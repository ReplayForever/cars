from rest_framework import serializers
from car_app.models import CarType


class CarTypeSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(read_only=True, source="brand.name")
    brand_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CarType
        fields = ("name", "brand", "brand_id")
