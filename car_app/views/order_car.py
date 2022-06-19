from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from car_app.models import OrderCar
from car_app.serializers import OrderCarSerializer


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

    def get_queryset(self):
        queryset = OrderCar.objects.all().order_by("-count")
        brand = self.request.query_params.get("brand")
        if brand is not None:
            queryset = queryset.filter(type__brand__name=brand)
        return queryset
