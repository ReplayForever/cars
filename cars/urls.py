"""cars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from car_app.views import *
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers


schema_view = get_swagger_view(title='Pastebin API')

router_brands = routers.SimpleRouter()
router_types = routers.SimpleRouter()
router_colors = routers.SimpleRouter()
router_orders = routers.SimpleRouter()
router_brands.register(r'brands', BrandViewSet)
router_types.register(r'types', CarTypeViewSet)
router_colors.register(r'colors', ColorViewSet)
router_orders.register(r'orders', OrderCarViewSet)


urlpatterns = [
    re_path(r'^$', schema_view, name='index'),
    path("admin/", admin.site.urls),
    path("api/v1/", include(router_brands.urls)),
    path("api/v1/", include(router_types.urls)),
    path("api/v1/", include(router_colors.urls)),
    path("api/v1/", include(router_orders.urls)),
]
