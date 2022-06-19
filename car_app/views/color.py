from rest_framework import viewsets

from car_app.models import Color
from car_app.serializers import ColorSerializer


class ColorsViewSet(viewsets.ModelViewSet):
    """
    Returns a list of available colors
    """

    queryset = Color.objects.all()
    serializer_class = ColorSerializer
