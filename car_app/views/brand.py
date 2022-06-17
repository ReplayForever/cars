from rest_framework import viewsets

from car_app.models import Brand
from car_app.serializers import BrandSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
