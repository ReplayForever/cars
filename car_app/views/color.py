from rest_framework import generics

from car_app.models import Color
from car_app.serializers import ColorSerializer


class ColorAPIList(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ColorAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
