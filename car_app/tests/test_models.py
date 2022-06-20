from django.test import TestCase

from car_app.models import Brand, CarType, Color, OrderCar


class CarModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.brand_1 = Brand.objects.create(name="VW", id=1)
        cls.type_1 = CarType.objects.create(name="Polo", brand_id=1, id=1)
        cls.color_1 = Color.objects.create(name="Black", id=1)
        cls.order_1 = OrderCar.objects.create(
            color_id=1, type_id=1, count=20, order_time="2022-06-19", id=1
        )

    def test_brand(self):
        data = str(self.brand_1)
        self.assertEqual(data, "VW")

    def test_color(self):
        data = str(self.color_1)
        self.assertEqual(data, "Black")

    def test_type(self):
        data = str(self.type_1)
        self.assertEqual(data, "Polo")

    def test_order(self):
        data = str(self.order_1)
        self.assertEqual(data, "1")
