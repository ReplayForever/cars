from rest_framework import generics

from car_app.models import OrderCar
from car_app.serializers import OrderCarSerializer


class OrderCarAPIList(generics.ListAPIView, generics.CreateAPIView):
    queryset = OrderCar.objects.all()
    serializer_class = OrderCarSerializer
