from rest_framework import viewsets

from car_app.models import Brand
from car_app.serializers import BrandSerializer


class BrandsViewSet(viewsets.ModelViewSet):
    """
    Returns a list of brands
    """

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
