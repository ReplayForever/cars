from rest_framework import generics
from django.shortcuts import render

from .serializers import OrderCarSerializer
from .models import ModelCar, Car, Color, OrderCar
from .serializers import ModelCarSerializer, CarSerializer, ColorSerializer


class ModelCarAPIList(generics.ListAPIView):
    queryset = ModelCar.objects.all()
    serializer_class = ModelCarSerializer


class CarAPIList(generics.ListAPIView, generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarAPIUpdate(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer



class ColorAPIList(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class OrderCarAPIList(generics.ListAPIView):
    queryset = OrderCar.objects.all()
    serializer_class = OrderCarSerializer
