from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from car_app.models import Brand, Color, CarType, OrderCar


class CarViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.brand_1 = Brand.objects.create(name='VW', id=1)
        cls.brand_2 = Brand.objects.create(name='BMW', id=2)
        cls.type_1 = CarType.objects.create(name='M3', brand_id=2, id=1)
        cls.type_2 = CarType.objects.create(name='Polo', brand_id=1, id=2)
        cls.color_1 = Color.objects.create(name='Black', id=1)
        cls.color_2 = Color.objects.create(name='White', id=2)
        cls.order_1 = OrderCar.objects.create(color_id=1, type_id=2, count=20, order_time='2022-06-19')
        cls.order_2 = OrderCar.objects.create(color_id=2, type_id=1, count=40, order_time='2022-05-15')
        cls.order_3 = OrderCar.objects.create(color_id=2, type_id=2, count=13, order_time='2022-06-01')

    def test_brand_view(self):
        expected_data = [
            {
                'name': 'VW'
            },
            {
                'name': 'BMW'
            }
        ]
        url = reverse('brands-list')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_color_view(self):
        url = reverse('colors-list')
        response = self.client.get(url)
        expected_data = [
            {
                'name': 'Black'
            },
            {
                'name': 'White'
            }
        ]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_type_view(self):
        expected_data = [
            {
                'name': 'M3',
                'brand': 'BMW'
            },
            {
                'name': 'Polo',
                'brand': 'VW'
            }
        ]
        url = reverse('types-list')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_order_view(self):
        expected_data = {
            "count": 3,
            "next": None,
            "previous": None,
            "results": [
                {
                    'color': 'White',
                    'type': 'M3',
                    'brand': 'BMW',
                    'count': 40,
                    'order_time': '2022-05-15'
                },
                {
                    'color': 'Black',
                    'type': 'Polo',
                    'brand': 'VW',
                    'count': 20,
                    'order_time': '2022-06-19'
                },
                {
                    'color': 'White',
                    'type': 'Polo',
                    'brand': 'VW',
                    'count': 13,
                    'order_time': '2022-06-01'
                }
            ]
        }
        url = reverse('orders-list')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_ordered_colors_view(self):
        expected_data = [
                {
                    'color': 'Black',
                    'count': 20
                },
                {
                    'color': 'White',
                    'count': 53
                }
        ]

        url = reverse('orders-list') + 'colors/'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_ordered_brand_view(self):
        expected_data = [
                {
                    'brand': 'BMW',
                    'count': 40
                },
                {
                    'brand': 'VW',
                    'count': 33
                }
        ]

        url = reverse('orders-list') + 'brands/?brand=VW'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_brand_filter_view(self):
        expected_data = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    'color': 'Black',
                    'type': 'Polo',
                    'brand': 'VW',
                    'count': 20,
                    'order_time': '2022-06-19'
                },
                {
                    'color': 'White',
                    'type': 'Polo',
                    'brand': 'VW',
                    'count': 13,
                    'order_time': '2022-06-01'
                }
            ]
        }

        url = reverse('orders-list') + '?brand=VW'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)
