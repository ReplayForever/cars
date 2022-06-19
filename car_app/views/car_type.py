from rest_framework import viewsets

from car_app.models import CarType
from car_app.serializers import CarTypeSerializer


class CarTypesViewSet(viewsets.ModelViewSet):
    """
    Returns a list of available types of car
    """

    queryset = CarType.objects.all()
    serializer_class = CarTypeSerializer
