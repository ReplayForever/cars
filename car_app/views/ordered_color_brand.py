from django.db.models import Sum, F
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from car_app.models import OrderCar
from car_app.serializers import OrderedColorBrandSerializer


class OrderedColorBrandViewSet(viewsets.ModelViewSet):
    """
    Returns a list of ordered colors and brands
    """

    serializer_class = OrderedColorBrandSerializer
    queryset = OrderCar.objects.all()

    @action(detail=False)
    def colors(self, request):
        """
        Returns a list of ordered colors
        """
        colors = OrderCar.objects.values("color__name").annotate(
            color=F("color_id__name"), count=Sum("count")
        )
        serializer = self.get_serializer(colors, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def brands(self, request):
        """
        Returns a list of ordered brands
        """
        brands = OrderCar.objects.values("type__brand").annotate(
            brand=F("type__brand__name"), count=Sum("count")
        )
        serializer = self.get_serializer(brands, many=True)
        return Response(serializer.data)
