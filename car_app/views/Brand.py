from rest_framework import generics

from car_app.models import Brand
from car_app.serializers import BrandSerializer


class BrandAPIList(generics.ListAPIView, generics.CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandAPIUpdate(generics.UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
