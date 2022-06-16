from rest_framework import serializers

from .models import ModelCar, Car, Color, OrderCar


class ModelCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelCar
        fields = ('model_car', 'car')


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('car',)


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('color',)


class OrderCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCar
        fields = ('color', 'model_car', 'count', 'order_time')
