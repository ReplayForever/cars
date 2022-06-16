from rest_framework import generics

from car_app.models import CarType
from car_app.serializers import CarTypeSerializer


class CarTypeAPIList(generics.ListAPIView, generics.CreateAPIView):
    queryset = CarType.objects.all()
    serializer_class = CarTypeSerializer
