from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from car_app.models import OrderCar, Brand, CarType
from car_app.serializers import OrderCarSerializer


class OrderCarPagination(PageNumberPagination):
    page_size = 10


class OrderCarViewSet(viewsets.ModelViewSet):
    queryset = OrderCar.objects.all()
    serializer_class = OrderCarSerializer
    pagination_class = OrderCarPagination

    # def get_queryset(self):
    #     pk = self.kwargs.get('pk')
    #     car_type = CarType.objects.all()
    #     if not pk:
    #         return Response({'car_type': car_type})

        # return CarType.objects.filter(pk=pk)
