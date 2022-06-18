from rest_framework import serializers
from car_app.models import CarType


class CarTypeSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(read_only=True)
    brand_id = serializers.IntegerField()

    class Meta:
        model = CarType
        fields = ("type", "brand", "brand_id")

    def create(self, validated_data):
        return CarType.objects.create(**validated_data)
