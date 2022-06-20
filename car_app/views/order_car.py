from django.db.models import F, Sum, QuerySet
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response

from car_app.models import OrderCar
from car_app.serializers import OrderCarSerializer, OrderedColorBrandSerializer


class OrderCarPagination(PageNumberPagination):
    page_size = 10


class OrderCarViewSet(viewsets.ModelViewSet):
    """
    Returns a sorted list of orders.
    You can filter list by brand.
    Note that code snippets are paginated to a maximum of 10 per page.
    """

    serializer_class = OrderCarSerializer
    pagination_class = OrderCarPagination

    def get_queryset(self) -> QuerySet:
        queryset = OrderCar.objects.all().order_by("-count")
        brand = self.request.query_params.get("brand")
        if brand is not None:
            queryset = queryset.filter(type__brand__name=brand)
        return queryset

    @action(detail=False)
    def colors(self, request: Request) -> Response:
        """
        Returns a list of ordered colors
        """
        colors = OrderCar.objects.values("color__name").annotate(
            color=F("color_id__name"), count=Sum("count")
        )
        serializer = OrderedColorBrandSerializer(colors, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def brands(self, request: Request) -> Response:
        """
        Returns a list of ordered brands
        """
        brands = OrderCar.objects.values("type__brand").annotate(
            brand=F("type__brand__name"), count=Sum("count")
        )
        serializer = OrderedColorBrandSerializer(brands, many=True)
        return Response(serializer.data)
