from rest_framework import generics

from car_app.models import Brand
from car_app.serializers import BrandSerializer


class BrandAPIList(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
