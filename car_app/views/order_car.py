from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from car_app.models import OrderCar
from car_app.serializers import OrderCarSerializer


class OrderCarPagination(PageNumberPagination):
    page_size = 10


class OrderCarViewSet(viewsets.ModelViewSet):
    queryset = OrderCar.objects.all()
    serializer_class = OrderCarSerializer
    pagination_class = OrderCarPagination
