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
from django.urls import path, re_path
from car_app.views import *
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    re_path(r'^$', schema_view, name='index'),
    path("admin/", admin.site.urls),
    path("api/v1/types/", CarTypeAPIList.as_view()),
    path("api/v1/types/<int:pk>", CarTypeAPIDetailView.as_view()),
    path("api/v1/brands/", BrandAPIList.as_view()),
    path("api/v1/brands/<int:pk>", BrandAPIDetailView.as_view()),
    path("api/v1/colors/", ColorAPIList.as_view()),
    path("api/v1/colors/<int:pk>", ColorAPIDetailView.as_view()),
    path("api/v1/orders/", OrderCarAPIList.as_view()),
    path("api/v1/orders/<int:pk>", OrderCarAPIDetailView.as_view()),
]
