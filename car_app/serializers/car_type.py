from rest_framework import serializers
from car_app.models import CarType


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = ("type", "brand")
