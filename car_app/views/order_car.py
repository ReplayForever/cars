from django.forms import model_to_dict
from rest_framework import viewsets, generics, status, request
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from car_app.models import OrderCar
from car_app.serializers import OrderCarSerializer


class OrderCarPagination(PageNumberPagination):
    page_size = 10


class OrderCarViewSet(viewsets.ModelViewSet):
    queryset = OrderCar.objects.all()
    serializer_class = OrderCarSerializer
    pagination_class = OrderCarPagination
