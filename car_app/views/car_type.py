from rest_framework import viewsets

from car_app.models import CarType
from car_app.serializers import CarTypeSerializer


class CarTypeViewSet(viewsets.ModelViewSet):
    queryset = CarType.objects.all()
    serializer_class = CarTypeSerializer

