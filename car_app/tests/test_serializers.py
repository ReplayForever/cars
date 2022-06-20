from django.test import TestCase

from car_app.models import Brand, Color, CarType, OrderCar
from car_app.serializers import (
    BrandSerializer,
    CarTypeSerializer,
    OrderCarSerializer,
    OrderedColorBrandSerializer,
)


class CarSerializersTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.brand_1 = Brand.objects.create(name="VW", id=1)
        cls.brand_2 = Brand.objects.create(name="BMW", id=2)
        cls.type_1 = CarType.objects.create(name="M3", brand_id=2, id=1)
        cls.type_2 = CarType.objects.create(name="Polo", brand_id=1, id=2)
        cls.color_1 = Color.objects.create(name="Black", id=1)
        cls.color_2 = Color.objects.create(name="White", id=2)
        cls.order_1 = OrderCar.objects.create(
            color_id=1, type_id=2, count=20, order_time="2022-06-19"
        )
        cls.order_2 = OrderCar.objects.create(
            color_id=2, type_id=1, count=40, order_time="2022-05-15"
        )
        cls.order_3 = OrderCar.objects.create(
            color_id=2, type_id=2, count=13, order_time="2022-06-01"
        )

    def test_brand_serializer(self):
        data = BrandSerializer([self.brand_1, self.brand_2], many=True).data
        expected_data = [{"name": "VW"}, {"name": "BMW"}]
        self.assertEqual(data, expected_data)

    def test_color_serializer(self):
        data = BrandSerializer([self.color_1, self.color_2], many=True).data
        expected_data = [{"name": "Black"}, {"name": "White"}]
        self.assertEqual(data, expected_data)

    def test_type_serializer(self):
        data = CarTypeSerializer([self.type_1, self.type_2], many=True).data
        expected_data = [
            {"name": "M3", "brand": "BMW"},
            {"name": "Polo", "brand": "VW"},
        ]
        self.assertEqual(data, expected_data)

    def test_order_serializer(self):
        data = OrderCarSerializer([self.order_1, self.order_2], many=True).data
        expected_data = [
            {
                "color": "Black",
                "type": "Polo",
                "brand": "VW",
                "count": 20,
                "order_time": "2022-06-19",
            },
            {
                "color": "White",
                "type": "M3",
                "brand": "BMW",
                "count": 40,
                "order_time": "2022-05-15",
            },
        ]
        self.assertEqual(data, expected_data)

    def test_ordered_color_brand_serializer(self):
        data = OrderedColorBrandSerializer([self.order_1, self.order_2], many=True).data
        expected_data = [
            {
                "color": "Black",
                "count": 20,
            },
            {
                "color": "White",
                "count": 40,
            },
        ]
        self.assertEqual(data, expected_data)
