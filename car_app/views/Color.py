from rest_framework import generics

from car_app.models import Color
from car_app.serializers import ColorSerializer


class ColorAPIList(generics.ListAPIView, generics.CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
