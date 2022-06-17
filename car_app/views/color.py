from rest_framework import viewsets

from car_app.models import Color
from car_app.serializers import ColorSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
