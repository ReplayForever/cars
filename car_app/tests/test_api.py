from django.forms import model_to_dict
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


from car_app.models import Brand, Color, CarType, OrderCar
from car_app.serializers import BrandSerializer


class CarAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.brand_1 = Brand.objects.create(name="VW")
        cls.type_1 = CarType.objects.create(name="M3", brand_id=1)
        cls.color_1 = Color.objects.create(name="Black")

    def test_brand_get(self):
        url = reverse("brands-list")
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_brand_post(self):
        url = reverse("brands-list")
        data = {"name": "Mercedes"}
        response = self.client.post(url, data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_color_get(self):
        url = reverse("colors-list")
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_color_post(self):
        url = reverse("colors-list")
        data = {"name": "Red"}
        response = self.client.post(url, data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_type_get(self):
        url = reverse("types-list")
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_type_post(self):
        url = reverse("types-list")
        data = {"name": "Passat", "brand_id": 1}
        response = self.client.post(url, data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_order_get(self):
        url = reverse("orders-list")
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_order_post(self):
        url = reverse("orders-list")
        data = {"color_id": 1, "type_id": 1, "count": 12}
        response = self.client.post(url, data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_ordered_color_get(self):
        url = reverse("orders-list") + "colors/"
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_ordered_brand_get(self):
        url = reverse("orders-list") + "brands/"
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
