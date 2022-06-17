from rest_framework import generics

from car_app.models import CarType
from car_app.serializers import CarTypeSerializer


class CarTypeAPIList(generics.ListCreateAPIView):
    queryset = CarType.objects.all()
    serializer_class = CarTypeSerializer


class CarTypeAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarType.objects.all()
    serializer_class = CarTypeSerializer
